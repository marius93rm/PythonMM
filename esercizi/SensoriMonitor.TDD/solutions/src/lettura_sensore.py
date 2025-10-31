"""Soluzione della milestone 1: rappresentazione di una lettura sensore."""

from __future__ import annotations

from datetime import datetime
from typing import Any


class LetturaSensore:
    """Incapsula i valori raccolti da un sensore IoT.

    La classe è immutabile dal punto di vista del chiamante: gli attributi sono
    esposti tramite proprietà in sola lettura così da favorire test e debugging.
    """

    def __init__(self, temperatura: float, umidita: float, timestamp: Any) -> None:
        self._temperatura = float(temperatura)
        self._umidita = float(umidita)
        if isinstance(timestamp, datetime):
            self._timestamp = timestamp
        elif isinstance(timestamp, str):
            # Consente timestamp ISO 8601 (es. 2024-01-01T10:30:00).
            self._timestamp = datetime.fromisoformat(timestamp)
        else:
            raise TypeError("timestamp deve essere datetime oppure stringa ISO")

    @property
    def temperatura(self) -> float:
        return self._temperatura

    @property
    def umidita(self) -> float:
        return self._umidita

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def __repr__(self) -> str:  # pragma: no cover - solo per debug
        return (
            "LetturaSensore("
            f"temperatura={self._temperatura}, "
            f"umidita={self._umidita}, "
            f"timestamp={self._timestamp.isoformat()})"
        )
