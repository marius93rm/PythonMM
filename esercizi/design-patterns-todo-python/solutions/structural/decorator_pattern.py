"""Soluzione commentata del pattern Decorator."""

from __future__ import annotations

from abc import ABC, abstractmethod


class DataSource(ABC):
    """Interfaccia di base per una sorgente dati."""

    @abstractmethod
    def read(self) -> str:
        """Restituisce i dati correnti."""

    @abstractmethod
    def write(self, data: str) -> None:
        """Aggiorna la sorgente con nuovi dati."""


class SimpleDataSource(DataSource):
    """Implementazione minima che salva dati in memoria."""

    def __init__(self) -> None:
        self._buffer: str = ""

    def read(self) -> str:
        return self._buffer

    def write(self, data: str) -> None:
        self._buffer = data


class LoggingDataSource(DataSource):
    """Decorator che logga le operazioni su una sorgente dati."""

    def __init__(self, wrapped: DataSource) -> None:
        self._wrapped = wrapped

    def read(self) -> str:
        print("[LOG] read requested")
        return self._wrapped.read()

    def write(self, data: str) -> None:
        print(f"[LOG] write: {data!r}")
        self._wrapped.write(data)


def make_logging_source() -> DataSource:
    """Factory helper che restituisce una sorgente con logging attivo."""
    return LoggingDataSource(SimpleDataSource())
