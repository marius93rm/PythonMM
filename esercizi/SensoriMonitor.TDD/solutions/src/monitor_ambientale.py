"""Soluzione commentata per MonitorAmbientale."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Protocol

from lettura_sensore import LetturaSensore


class Notificatore(Protocol):
    """Interfaccia attesa dal monitor (Protocol per supportare i mock)."""

    def manda_alert(self, messaggio: str) -> None:
        ...


@dataclass(frozen=True)
class SoglieAllarme:
    temperatura_massima: float = 50.0
    umidita_minima: float = 20.0


class MonitorAmbientale:
    """Gestisce lo storico delle letture e la logica di allarme."""

    def __init__(self, notificatore: Optional[Notificatore] = None) -> None:
        self._letture: List[LetturaSensore] = []
        self._notificatore = notificatore
        self._soglie = SoglieAllarme()

    def aggiungi_lettura(self, lettura: LetturaSensore) -> None:
        self._letture.append(lettura)
        self._notifica_se_necessario(lettura)

    def tutte_le_letture(self) -> Iterable[LetturaSensore]:
        return tuple(self._letture)

    def _verifica_soglie(self, lettura: LetturaSensore) -> bool:
        return bool(
            lettura.temperatura > self._soglie.temperatura_massima
            or lettura.umidita < self._soglie.umidita_minima
        )

    def is_allarme(self, lettura: LetturaSensore) -> bool:
        return self._verifica_soglie(lettura)

    def _notifica_se_necessario(self, lettura: LetturaSensore) -> None:
        if self._notificatore is None:
            return
        if not self.is_allarme(lettura):
            return
        messaggio = (
            "Allarme rilevato: "
            f"temperatura={lettura.temperatura:.1f}, "
            f"umidita={lettura.umidita:.1f}"
        )
        self._notificatore.manda_alert(messaggio)
