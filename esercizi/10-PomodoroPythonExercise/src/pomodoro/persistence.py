from __future__ import annotations
from typing import Protocol, Literal
from dataclasses import dataclass
from datetime import datetime
import csv
import os

@dataclass
class SessionLog:
    started_at: datetime
    kind: Literal["focus", "break"]
    seconds: int

class ISessionRepository(Protocol):
    def save(self, log: SessionLog) -> None: ...

class CsvSessionRepository:
    """
    Salva un file CSV appendendo le sessioni.
    SRP: sola persistenza; DIP: interfaccia ISessionRepository.
    """
    def __init__(self, path: str = "sessions.csv") -> None:
        self.path = path
        # crea header se file non esiste
        if not os.path.exists(self.path):
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["started_at_iso", "kind", "seconds"])

    def save(self, log: SessionLog) -> None:
        """
        TODO M5: salvare una riga con:
        - started_at_iso = log.started_at.isoformat()
        - kind = "focus" | "break"
        - seconds = int
        """
        # TODO: implementare l'append su CSV come descritto
        raise NotImplementedError("Implementa CsvSessionRepository.save (Milestone 5)")
