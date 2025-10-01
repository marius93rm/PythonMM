
# esercizio2_hr_system.py
# ============================================================
# Esercizio 2 — Sistema di Gestione Risorse Umane (fino alla slide 33)
# Obiettivo: usare OOP (classi, metodi, __init__/__str__/__repr__, attributi di
# classe/istanza, property, ereditarietà singola+multipla, overriding, super(),
# duck typing e polimorfismo).
#
# Istruzioni:
# - Implementa i TODO SENZA modificare i test.
# - Esegui il file per vedere il report:
#     test eseguiti / test superati / test falliti
# - Mantieni il codice chiaro e mantenibile.
# ============================================================

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional


# =========================
# Sezione 1: Base model
# =========================

class Persona:
    """Rappresenta una persona generica.

    Requisiti:
    - Attributo di CLASSE: popolazione (conteggio istanze create).
    - __init__(self, nome: str, eta: int)
      * usa property per 'eta' (validazione: 0 <= eta <= 120, altrimenti ValueError)
      * normalizza 'nome' con title case e spazi singoli.
    - __repr__ -> Persona('Mario Rossi', 30)
    - __str__  -> Mario Rossi (30)
    - Metodo di istanza: lavora(self) -> str
      * default: "Persona generica al lavoro" (sarà overridato)
    - Metodo di classe: from_dict(cls, d: Dict[str, Any]) -> Persona
      * accetta {'nome': str, 'eta': int}
    - Metodo statico: normalize_name(s: str) -> str
      * rimuove spazi eccessivi e applica title case
    """

    popolazione: int = 0  # TODO: incrementare nel costruttore

    def __init__(self, nome: str, eta: int):
        # TODO: normalizza nome, setta eta tramite property, incrementa popolazione
        raise NotImplementedError

    def __repr__(self) -> str:
        # TODO
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO
        raise NotImplementedError

    @property
    def eta(self) -> int:
        # TODO getter
        raise NotImplementedError

    @eta.setter
    def eta(self, value: int) -> None:
        # TODO validazione 0 <= value <= 120
        raise NotImplementedError

    def lavora(self) -> str:
        # TODO implementazione base
        raise NotImplementedError

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Persona:
        # TODO
        raise NotImplementedError

    @staticmethod
    def normalize_name(s: str) -> str:
        # TODO
        raise NotImplementedError


# =========================
# Sezione 2: Dipendenti
# =========================

class Dipendente(Persona):
    """Dipendente aziendale.

    Requisiti aggiuntivi:
    - __init__(self, nome: str, eta: int, ruolo: str, stipendio_lordo: float)
      * chiama super().__init__(...)
      * property 'stipendio_lordo' con validazione: >= 0
      * 'ruolo' normalizzato (title case, spazi singoli)
    - __str__  -> "Mario Rossi (30) — Sviluppatore — 40000.0 € lordi"
    - override lavora() -> "Mario Rossi sta lavorando come Sviluppatore"
    - Metodo di classe: junior(cls, nome: str, eta: int, ruolo: str) -> Dipendente
      * factory con stipendio_lordo predefinito: 25000.0
    - Metodo statico: netto_da_lordo(lordo: float, aliquota: float) -> float
      * calcola netto = lordo * (1 - aliquota), senza arrotondare
    """

    def __init__(self, nome: str, eta: int, ruolo: str, stipendio_lordo: float):
        # TODO
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO
        raise NotImplementedError

    def lavora(self) -> str:
        # TODO
        raise NotImplementedError

    @property
    def stipendio_lordo(self) -> float:
        # TODO getter
        raise NotImplementedError

    @stipendio_lordo.setter
    def stipendio_lordo(self, value: float) -> None:
        # TODO validazione
        raise NotImplementedError

    @classmethod
    def junior(cls, nome: str, eta: int, ruolo: str) -> Dipendente:
        # TODO
        raise NotImplementedError

    @staticmethod
    def netto_da_lordo(lordo: float, aliquota: float) -> float:
        # TODO
        raise NotImplementedError


# =========================
# Sezione 3: Mixin & Manager
# =========================

class MentorMixin:
    """Mixin che aggiunge capacità di mentoring.

    Requisiti:
    - __init__(self, *args, mentees: Optional[List[str]] = None, **kwargs)
      * compatibile con super() cooperativo
      * salva una lista di mentee (nomi normalizzati) in self.mentees
    - metodo: aggiungi_mentee(self, nome: str) -> None
    - __str__: NON override qui. Lascia alle classi principali.
    """

    def __init__(self, *args, mentees: Optional[List[str]] = None, **kwargs):
        # TODO: super cooperativo + salva mentees
        raise NotImplementedError

    def aggiungi_mentee(self, nome: str) -> None:
        # TODO: aggiungi nome normalizzato se non presente
        raise NotImplementedError


class Manager(MentorMixin, Dipendente):
    """Manager che è anche Mentor.
    (Ereditarietà multipla: MentorMixin prima di Dipendente per precedenza MRO.)

    Requisiti aggiuntivi:
    - __init__(self, nome: str, eta: int, ruolo: str, stipendio_lordo: float,
               mentees: Optional[List[str]] = None)
      * costruttore COOPERATIVO con super()
    - override lavora() -> "<nome> coordina come <ruolo> (mentees: N)"
    - __repr__ -> Manager('Mario Rossi', 40, 'Team Lead', 60000.0, mentees=2)
    """

    def __init__(self, nome: str, eta: int, ruolo: str, stipendio_lordo: float,
                 mentees: Optional[List[str]] = None):
        # TODO: chiamata cooperativa a super()
        raise NotImplementedError

    def lavora(self) -> str:
        # TODO
        raise NotImplementedError

    def __repr__(self) -> str:
        # TODO
        raise NotImplementedError


# =========================
# Sezione 4: Duck typing
# =========================

def turni_giornalieri(lavoratori: Iterable[Any]) -> List[str]:
    """Dato un iterabile di oggetti, chiama .lavora() su ognuno e raccogli i messaggi.
    Requisiti:
    - NON controllare il tipo (duck typing). Ignora gli oggetti senza .lavora().
    - Mantieni l'ordine di input.
    """
    # TODO
    raise NotImplementedError


# =========================
# Sezione 5: Test
# =========================

class _T:
    ok = 0
    fail = 0
    total = 0

def _assert(name: str, cond: bool):
    _T.total += 1
    if cond:
        _T.ok += 1
    else:
        _T.fail += 1
        print(f"❌ Test fallito: {name}")

def _run_tests():
    d = None
    m = None
    print("\n== Avvio test esercizio 2 (HR System) ==")

    # Persona
    try:
        p = Persona("  mario   rossi ", 30)
        _assert("Persona.__str__", str(p) == "Mario Rossi (30)")
        _assert("Persona.__repr__", repr(p) == "Persona('Mario Rossi', 30)")
        _assert("Persona.lavora base", p.lavora() == "Persona generica al lavoro")
        _assert("Persona.popolazione>=1", Persona.popolazione >= 1)
        try:
            p.eta = 130
            _assert("Persona.eta invalid", False)
        except ValueError:
            _assert("Persona.eta invalid raises", True)
        p.eta = 31
        _assert("Persona.eta setter", p.eta == 31)
        p2 = Persona.from_dict({"nome": "  anna bianchi ", "eta": 25})
        _assert("Persona.from_dict", isinstance(p2, Persona) and str(p2) == "Anna Bianchi (25)")
        _assert("normalize_name", Persona.normalize_name("  luCA   de  luca ") == "Luca De Luca")
    except Exception:
        _assert("Persona blocco", False)

    # Dipendente
    try:
        d = Dipendente("Mario Rossi", 30, "sviluppatore", 40000.0)
        _assert("Dipendente.__str__", str(d) == "Mario Rossi (30) — Sviluppatore — 40000.0 € lordi")
        _assert("Dipendente.lavora", d.lavora() == "Mario Rossi sta lavorando come Sviluppatore")
        d.stipendio_lordo = 41000.0
        _assert("Dipendente.stipendio setter", d.stipendio_lordo == 41000.0)
        dj = Dipendente.junior("Anna Bianchi", 25, "tester")
        _assert("Dipendente.junior", isinstance(dj, Dipendente) and dj.stipendio_lordo == 25000.0)
        _assert("Dipendente.netto_da_lordo", Dipendente.netto_da_lordo(1000.0, 0.22) == 780.0)
    except Exception:
        _assert("Dipendente blocco", False)

    # Mentor + Manager (ereditarietà multipla)
    try:
        m = Manager("Laura Verdi", 40, "Team Lead", 60000.0, mentees=["  mario  rossi", "anna bianchi"])
        _assert("Manager.isinstance", isinstance(m, MentorMixin) and isinstance(m, Dipendente))
        _assert("Manager.__repr__", repr(m) == "Manager('Laura Verdi', 40, 'Team Lead', 60000.0, mentees=2)")
        _assert("Manager.lavora", m.lavora() == "Laura Verdi coordina come Team Lead (mentees: 2)")
        m.aggiungi_mentee(" MARCO  blu ")
        _assert("Mentor.aggiungi_mentee", m.mentees[-1] == "Marco Blu" and len(m.mentees) == 3)
    except Exception:
        _assert("Manager blocco", False)

    # Duck typing turni_giornalieri
    class Freelance:
        def __init__(self, nome):
            # Non dipendere dall'implementazione dello studente; fallback locale
            try:
                self.nome = Persona.normalize_name(nome)
            except Exception:
                s = " ".join(str(nome).split()).title()
                self.nome = s
        def lavora(self): return f"{self.nome} lavora da freelance"

    items = []
    if d is not None:
        items.append(d)
    if m is not None:
        items.append(m)
    items.extend([Freelance("  giorgia  neri"), object()])
    out = turni_giornalieri(items)
    if d is not None and m is not None:
        _assert("turni_giornalieri size", len(out) == 3)
        _assert("turni_giornalieri order", out[0].endswith("Sviluppatore") and out[-1] == "Giorgia Neri lavora da freelance")
    else:
        # fallback: verifica minimo comportamento duck-typed senza esplodere
        _assert("turni_giornalieri fallback size>=1", len(out) >= 1)
        _assert("turni_giornalieri fallback last", out[-1] == "Giorgia Neri lavora da freelance")

    # Riepilogo
    print("\n===== RISULTATO TEST =====")
    print(f"test eseguiti: {_T.total}")
    print(f"test superati: {_T.ok}")
    print(f"test falliti:  {_T.fail}")
    print("==========================\n")

if __name__ == "__main__":
    _run_tests()
