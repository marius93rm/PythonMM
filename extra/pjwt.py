# ===========================
# app.py — Flask + JWT (demo)
# ===========================

from datetime import datetime, timedelta, timezone   # importiamo date/ora per scadenza token
from functools import wraps                          # per creare decorator (jwt_required, role_required)
from typing import Optional, Callable, Any, Dict     # tipi per annotazioni (facoltativo ma utile)

import jwt                                           # PyJWT: codifica/decodifica JSON Web Token
from flask import Flask, request, jsonify            # Flask base: app, richiesta, risposta JSON
from werkzeug.security import generate_password_hash, check_password_hash  # hashing password

app = Flask(__name__)                                # istanziamo l’app Flask

# -----------------------
# Config di autenticazione
# -----------------------
JWT_SECRET = "cambia-questa-chiave-super-segreta"    # chiave segreta: in produzione usa variabile d'ambiente
JWT_ALG = "HS256"                                    # algoritmo di firma per JWT
JWT_EXPIRES_MIN = 30                                 # durata del token in minuti

# ---------------------
# Finto "database" utenti
# ---------------------
USERS = {                                            # dizionario username -> info
    "mario": {"pwd_hash": generate_password_hash("p4ssw0rd"), "role": "user"},  # utente standard
    "admin": {"pwd_hash": generate_password_hash("admin123"), "role": "admin"}, # utente admin
}

# -----------------------
# Utility per i JSON Web Token
# -----------------------
def create_access_token(identity: str, role: str) -> str:
    """Crea un JWT con subject (utente), ruolo e scadenza."""
    now = datetime.now(tz=timezone.utc)             # timestamp attuale in UTC
    payload = {                                     # contenuto (claims) del token
        "sub": identity,                            # 'subject' = username
        "role": role,                               # claim personalizzata: ruolo
        "iat": int(now.timestamp()),                # 'issued at' (quando è stato emesso)
        "exp": int((now + timedelta(minutes=JWT_EXPIRES_MIN)).timestamp()),  # 'expiration'
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)  # firma e restituisce il token (stringa)

def decode_token(token: str) -> Dict[str, Any]:
    """Verifica e decodifica un JWT, lancia eccezioni se non valido/expired."""
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG]) # decodifica con verifica firma/exp

def _get_bearer_token() -> Optional[str]:
    """Estrae il token dal header Authorization: Bearer <token>."""
    auth = request.headers.get("Authorization", "") # recupera header Authorization o stringa vuota
    if auth.startswith("Bearer "):                  # controlla prefisso 'Bearer '
        return auth.split(" ", 1)[1].strip()        # estrae la parte del token
    return None                                     # se non presente, None

# -----------------------
# Decorator: JWT richiesto
# -----------------------
def jwt_required(fn: Callable) -> Callable:
    """Decorator che richiede un token valido per accedere alla route."""
    @wraps(fn)                                      # preserva metadati della funzione originale
    def wrapper(*args, **kwargs):                   # wrapper che sostituisce la funzione
        token = _get_bearer_token()                 # prova a leggere il token dal header
        if not token:                               # se manca il token
            return jsonify({"error": "Missing Bearer token"}), 401  # 401 Unauthorized
        try:
            claims = decode_token(token)            # decodifica e valida il token
            # salviamo le info utente nel contesto della richiesta
            request.user = {                        # attach semplice: in app reali usare g/ctx
                "username": claims["sub"],          # username dal claim 'sub'
                "role": claims.get("role", "user"), # ruolo (default 'user' se assente)
            }
        except jwt.ExpiredSignatureError:           # token scaduto
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:               # token non valido (firma/struttura)
            return jsonify({"error": "Invalid token"}), 401
        return fn(*args, **kwargs)                  # esegue la funzione originale se tutto ok
    return wrapper                                  # restituisce il decorator pronto

# --------------------------
# Decorator: ruolo richiesto
# --------------------------
def role_required(required_role: str) -> Callable:
    """Decorator che richiede un ruolo esatto (es. 'admin')."""
    def decorator(fn: Callable) -> Callable:        # factory che riceve la funzione da decorare
        @wraps(fn)
        def wrapper(*args, **kwargs):
            token = _get_bearer_token()             # legge il token
            if not token:                           # se manca, 401
                return jsonify({"error": "Missing Bearer token"}), 401
            try:
                claims = decode_token(token)        # decodifica/valida token
            except jwt.InvalidTokenError:           # qualsiasi invalidità
                return jsonify({"error": "Invalid token"}), 401

            role = claims.get("role")               # estrae ruolo dalle claims
            if role != required_role:               # confronto ruolo richiesto vs. effettivo
                return jsonify({"error": "Forbidden"}), 403  # 403 se non autorizzato
            request.user = {                        # salva utente nel contesto richiesta
                "username": claims["sub"],
                "role": role,
            }
            return fn(*args, **kwargs)              # esegue la funzione originale
        return wrapper
    return decorator

# -------------
# Route: /auth/login
# -------------
@app.post("/auth/login")                            # endpoint POST per autenticarsi
def login():
    data = request.get_json(silent=True) or {}      # legge JSON body (silenzioso se non valido)
    username = data.get("username")                 # prende username
    password = data.get("password")                 # prende password
    if not username or not password:                # validazione presenza campi
        return jsonify({"error": "username and password required"}), 400

    user = USERS.get(username)                      # cerca utente nel "DB"
    # verifica utente esiste e password corretta (hash)
    if not user or not check_password_hash(user["pwd_hash"], password):
        return jsonify({"error": "invalid credentials"}), 401

    token = create_access_token(identity=username, role=user["role"])  # crea JWT
    # restituisce JSON con token, tipo e durata in secondi
    return jsonify({
        "access_token": token,
        "token_type": "Bearer",
        "expires_in": JWT_EXPIRES_MIN * 60
    })

# ----------------
# Route protetta: /api/me
# ----------------
@app.get("/api/me")                                 # endpoint GET
@jwt_required                                       # richiede un token valido
def me():
    return jsonify({"user": request.user})          # ritorna info utente dal contesto

# -------------------------
# Route solo admin: /api/admin/secret
# -------------------------
@app.get("/api/admin/secret")                       # endpoint GET
@role_required("admin")                             # consenti accesso solo a ruolo 'admin'
def admin_only():
    return jsonify({"secret": "solo admin", "user": request.user})  # payload demo

# -------------
# Bootstrap app
# -------------
if __name__ == "__main__":                          # esecuzione diretta (non import come modulo)
    app.run(debug=True)                             # avvia dev server Flask (debug=True per sviluppo)
