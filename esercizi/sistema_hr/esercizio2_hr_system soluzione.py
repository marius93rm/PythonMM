# esercizio2_hr_system.py
from __future__ import annotations
from typing import Any, Dict, Iterable, List, Optional


# =========================
# Sezione 1: Base model
# =========================

class Persona:
    popolazione: int = 0  # attributo di classe

    def __init__(self, nome: str, eta: int):
        # Normalizziamo subito il nome
        self.nome = Persona.normalize_name(nome)
        # Validazione dell'età tramite property
        self.eta = eta
        # Incremento della popolazione
        Persona.popolazione += 1

    def __repr__(self) -> str:
        # Rappresentazione tecnica (per debug/repr)
        return f"Persona({self.nome!r}, {self.eta})"

    def __str__(self) -> str:
        # Rappresentazione leggibile
        return f"{self.nome} ({self.eta})"

    @property
    def eta(self) -> int:
        return self._eta

    @eta.setter
    def eta(self, value: int) -> None:
        if not (0 <= value <= 120):
            raise ValueError("Età non valida")
        self._eta = value

    def lavora(self) -> str:
        # Metodo base, sarà overridato nelle sottoclassi
        return "Persona generica al lavoro"

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Persona:
        # Factory da dizionario
        return cls(d["nome"], d["eta"])

    @staticmethod
    def normalize_name(s: str) -> str:
        # Elimina spazi multipli e applica Title Case
        return " ".join(s.split()).title()


# =========================
# Sezione 2: Dipendenti
# =========================

class Dipendente(Persona):
    def __init__(self, nome: str, eta: int, ruolo: str, stipendio_lordo: float):
        # Chiamata al costruttore di Persona
        super().__init__(nome, eta)
        # Normalizzazione del ruolo
        self.ruolo = Persona.normalize_name(ruolo)
        # Validazione stipendio tramite property
        self.stipendio_lordo = stipendio_lordo

    def __str__(self) -> str:
        return f"{self.nome} ({self.eta}) — {self.ruolo} — {self.stipendio_lordo} € lordi"

    def lavora(self) -> str:
        return f"{self.nome} sta lavorando come {self.ruolo}"

    @property
    def stipendio_lordo(self) -> float:
        return self._stipendio_lordo

    @stipendio_lordo.setter
    def stipendio_lordo(self, value: float) -> None:
        if value < 0:
            raise ValueError("Stipendio non valido")
        self._stipendio_lordo = value

    @classmethod
    def junior(cls, nome: str, eta: int, ruolo: str) -> Dipendente:
        # Factory con stipendio fisso
        return cls(nome, eta, ruolo, 25000.0)

    @staticmethod
    def netto_da_lordo(lordo: float, aliquota: float) -> float:
        return lordo * (1 - aliquota)


# =========================
# Sezione 3: Mixin & Manager
# =========================

class MentorMixin:
    def __init__(self, *args, mentees: Optional[List[str]] = None, **kwargs):
        # super cooperativo per mantenere la MRO
        super().__init__(*args, **kwargs)
        self.mentees = []
        if mentees:
            for nome in mentees:
                self.mentees.append(Persona.normalize_name(nome))

    def aggiungi_mentee(self, nome: str) -> None:
        norm = Persona.normalize_name(nome)
        if norm not in self.mentees:
            self.mentees.append(norm)


class Manager(MentorMixin, Dipendente):
    def __init__(self, nome: str, eta: int, ruolo: str, stipendio_lordo: float,
                 mentees: Optional[List[str]] = None):
        # Costruttore cooperativo
        super().__init__(nome, eta, ruolo, stipendio_lordo, mentees=mentees)

    def lavora(self) -> str:
        return f"{self.nome} coordina come {self.ruolo} (mentees: {len(self.mentees)})"

    def __repr__(self) -> str:
        return f"Manager({self.nome!r}, {self.eta}, {self.ruolo!r}, {self.stipendio_lordo}, mentees={len(self.mentees)})"


# =========================
# Sezione 4: Duck typing
# =========================

def turni_giornalieri(lavoratori: Iterable[Any]) -> List[str]:
    out = []
    for w in lavoratori:
        # Duck typing: proviamo a chiamare lavora() se esiste
        if hasattr(w, "lavora") and callable(w.lavora):
            try:
                out.append(w.lavora())
            except Exception:
                continue
    return out