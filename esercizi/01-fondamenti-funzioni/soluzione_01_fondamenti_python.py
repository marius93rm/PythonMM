def pulisci_nomi_clienti(nomi: list[str]) -> list[str]:
    # Creiamo un set per ricordare quali nomi normalizzati abbiamo già visto
    visti = set()
    # Lista di output nell'ordine di primo incontro
    out: list[str] = []
    for raw in nomi:
        # 1) rimuovi spazi iniziali/finali
        trimmed = raw.strip()
        # 2) comprimi gli spazi interni multipli usando split() + join()
        #    split() senza argomenti spacchetta su qualsiasi sequenza di spazi
        compresso = " ".join(trimmed.split())
        # 3) porta a "Nome Cognome" con iniziali maiuscole
        norm = compresso.title()
        # 4) evita duplicati mantenendo il primo incontro
        if norm and norm not in visti:
            visti.add(norm)
            out.append(norm)
    return out


def password_valide(passwords: Iterable[str]) -> set[str]:
    # Usiamo un set perché il risultato richiesto è un insieme di password valide
    valid: set[str] = set()
    for pw in passwords:
        # Verifica che sia stringa, lunghezza minima, contenga almeno una lettera e una cifra
        if (
            isinstance(pw, str)
            and len(pw) >= 8
            and any(c.isalpha() for c in pw)   # almeno una lettera
            and any(c.isdigit() for c in pw)   # almeno una cifra
        ):
            valid.add(pw)
    return valid


def conteggia_accessi_ok(log: list[tuple[str, int]]) -> dict[str, int]:
    # Dizionario utente -> conteggio status 200
    out: dict[str, int] = {}
    for utente, status in log:
        # Contiamo solo le risposte con codice 200
        if status == 200:
            # get(..., 0) recupera il conteggio corrente o 0 se non esiste
            out[utente] = out.get(utente, 0) + 1
    return out


def media_pesata(voti: dict[str, tuple[int, int]]) -> float:
    # Calcoliamo numeratore: somma(voto * crediti)
    num = sum(v * c for v, c in voti.values())
    # Calcoliamo denominatore: somma(crediti)
    den = sum(c for _, c in voti.values()) # _ perché il voto non serve qui
    # Se nessun credito, la media è 0.0 per evitare divisione per zero
    return num / den if den > 0 else 0.0


def unisci_inventari(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    # Copiamo 'a' per non modificarlo (richiesto)
    out = a.copy()
    # Sommiamo le quantità di 'b' chiave per chiave
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return out


def punteggio_priorita(etichetta: str) -> int:
    # Normalizziamo a minuscolo per robustezza
    match (etichetta or "").lower():
        case "critica":
            return 3
        case "alta":
            return 2
        case "media":
            return 1
        case "bassa":
            return 0
        # Qualsiasi altro valore mappato a 0
        case _:
            return 0


def ordina_task_per_priorita(task: list[tuple[str, str]]) -> list[tuple[str, str]]:
    # Ordiniamo decrescente per priorità: usiamo -punteggio come chiave primaria
    # In caso di parità, ordiniamo alfabeticamente per titolo in modo case-insensitive
    return sorted(
        task,
        key=lambda t: (-punteggio_priorita(t[1]), t[0].lower())
    )


def riepilogo_bilancio(transazioni: list[dict[str, Any]]) -> dict[str, float]:
    # Accumulatori per totali
    tot_entrate = 0.0
    tot_uscite = 0.0
    # Sotto-dizionario per categoria con segno: + per entrate, - per uscite
    per_cat: dict[str, float] = {}
    for tx in transazioni:
        cat = tx["categoria"]
        imp = float(tx["importo"])
        tipo = tx["tipo"]
        if tipo == "entrata":
            # Aggiorna totali e categoria in positivo
            tot_entrate += imp
            per_cat[cat] = per_cat.get(cat, 0.0) + imp
        else:
            # Aggiorna totali e categoria: le uscite sono conteggiate negative nel breakdown
            tot_uscite += imp
            per_cat[cat] = per_cat.get(cat, 0.0) - imp
    # Saldo = entrate - uscite (uscite sono positive nel totale)
    saldo = tot_entrate - tot_uscite
    return {
        "totale_entrate": tot_entrate,
        "totale_uscite": tot_uscite,
        "saldo": saldo,
        "per_categoria": per_cat,
    }


def estrai_keyword(testi: Iterable[str], stopwords: set[str], minimo: int = 4) -> set[str]:
    # Normalizziamo le stopword a minuscolo per confronto coerente
    stop = {s.lower() for s in stopwords}
    out: set[str] = set()
    for frase in testi:
        # Per ogni frase spezzettiamo in token separati da spazi
        for tok in (frase or "").lower().split():
            # Teniamo solo token alfanumerici, non presenti tra le stopword,
            # e di lunghezza almeno 'minimo'
            if tok.isalnum() and len(tok) >= minimo and tok not in stop:
                out.add(tok)
    return out


def primo_quadrato_maggiore_di(numeri: list[int], soglia: int) -> tuple[int, int] | None:
    # Scorriamo con indice e valore
    for i, n in enumerate(numeri):
        # Usiamo il walrus operator per calcolare una sola volta il quadrato
        if (q := n * n) > soglia:
            # Ritorniamo valore e indice del primo che supera la soglia
            return (n, i)
    # Nessun elemento soddisfa la condizione
    return None


def raggruppa_anagrammi(parole: Iterable[str]) -> dict[tuple[str, ...], list[str]]:
    # Dizionario: chiave = tupla di lettere ordinate, valore = lista di parole nell'ordine di arrivo
    gruppi: dict[tuple[str, ...], list[str]] = {}
    for p in parole:
        # Normalizziamo a minuscolo e ordiniamo le lettere per costruire la chiave
        key = tuple(sorted((p or "").lower()))
        # Inseriamo la parola originale nel gruppo corrispondente
        gruppi.setdefault(key, []).append(p)
    return gruppi
