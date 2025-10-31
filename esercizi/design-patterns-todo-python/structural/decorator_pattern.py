"""Pattern Decorator
===================
Cos'è il pattern:
    Il Decorator avvolge un oggetto per aggiungere responsabilità extra mantenendo la stessa interfaccia.
Obiettivo didattico:
    Capire come comporre comportamenti dinamicamente senza modificare la classe originale.
Scenario proposto:
    Una sorgente dati deve poter loggare le letture e le scritture senza cambiare l'implementazione base.
Cosa deve fare lo studente:
    Implementare l'interfaccia `DataSource`, creare la versione semplice e quella con logging.
Passi TODO:
    1. Definire i metodi astratti `read` e `write`.
    2. Completare `SimpleDataSource` per gestire uno storage interno minimale.
    3. Realizzare `LoggingDataSource` che avvolge un'altra fonte e aggiunge messaggi di log.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol


class DataSource(ABC):
    """Interfaccia di base per una sorgente dati."""

    # TODO: definire metodi astratti read() -> str e write(data: str) -> None


class SimpleDataSource(DataSource):
    """Implementazione minima che salva dati in memoria."""

    def __init__(self) -> None:
        self._buffer: str = ""

    def read(self) -> str:
        # TODO: restituire il contenuto attuale
        raise NotImplementedError("Implementare read nella sorgente semplice")

    def write(self, data: str) -> None:
        # TODO: salvare il contenuto nella variabile interna
        raise NotImplementedError("Implementare write nella sorgente semplice")


class LoggingDataSource(DataSource):
    """Decorator che logga le operazioni su una sorgente dati."""

    def __init__(self, wrapped: DataSource) -> None:
        self._wrapped = wrapped

    def read(self) -> str:
        # TODO: aggiungere un log prima di delegare a wrapped.read()
        raise NotImplementedError("Implementare read con logging")

    def write(self, data: str) -> None:
        # TODO: loggare e poi chiamare wrapped.write(data)
        raise NotImplementedError("Implementare write con logging")


def make_logging_source() -> DataSource:
    """Factory helper che restituisce una sorgente con logging attivo."""
    # TODO: creare un SimpleDataSource e avvolgerlo con LoggingDataSource
    raise NotImplementedError("Creare una catena di decorator")
