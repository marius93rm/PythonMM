"""Pattern Chain of Responsibility
==================================
Cos'è il pattern:
    La Chain of Responsibility inoltra una richiesta lungo una catena di handler finché uno la gestisce.
Obiettivo didattico:
    Creare una catena di logger che decidono se processare il messaggio in base al livello.
Scenario proposto:
    Dobbiamo gestire messaggi INFO, WARNING ed ERROR con handler dedicati che possono passare la palla.
Cosa deve fare lo studente:
    Completare la catena definendo il comportamento di ciascun handler e collegandoli.
Passi TODO:
    1. Implementare la classe base `LogHandler` con riferimento al successivo e metodo `handle`.
    2. Creare handler concreti che verificano il livello del messaggio.
    3. Fornire una funzione di setup che colleghi gli handler nell'ordine corretto.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class LogMessage:
    """Rappresenta un messaggio di log con un livello e un testo."""

    level: str
    text: str


class LogHandler(ABC):
    """Handler base della catena."""

    def __init__(self) -> None:
        self._next: Optional["LogHandler"] = None

    def set_next(self, handler: "LogHandler") -> "LogHandler":
        self._next = handler
        return handler

    def handle(self, message: LogMessage) -> None:
        # TODO: definire il comportamento di default: passare al prossimo handler se presente
        raise NotImplementedError("Implementare handle di base")

    @abstractmethod
    def _can_handle(self, message: LogMessage) -> bool:
        """Determina se l'handler gestisce il messaggio."""

    @abstractmethod
    def _process(self, message: LogMessage) -> None:
        """Contiene la logica specifica del livello di log."""


class InfoLogHandler(LogHandler):
    """Gestisce i messaggi di livello INFO."""

    def _can_handle(self, message: LogMessage) -> bool:
        # TODO: controllare il livello INFO
        raise NotImplementedError("Implementare controllo livello INFO")

    def _process(self, message: LogMessage) -> None:
        # TODO: simulare l'elaborazione (es. accumulare, stampare, ecc.)
        raise NotImplementedError("Implementare process per INFO")


class WarningLogHandler(LogHandler):
    """Gestisce i messaggi di livello WARNING."""

    def _can_handle(self, message: LogMessage) -> bool:
        # TODO: controllare il livello WARNING
        raise NotImplementedError("Implementare controllo livello WARNING")

    def _process(self, message: LogMessage) -> None:
        # TODO: simulare l'elaborazione per warning
        raise NotImplementedError("Implementare process per WARNING")


class ErrorLogHandler(LogHandler):
    """Gestisce i messaggi di livello ERROR."""

    def _can_handle(self, message: LogMessage) -> bool:
        # TODO: controllare il livello ERROR
        raise NotImplementedError("Implementare controllo livello ERROR")

    def _process(self, message: LogMessage) -> None:
        # TODO: simulare l'elaborazione per errori critici
        raise NotImplementedError("Implementare process per ERROR")


def build_logging_chain() -> LogHandler:
    """Crea e collega gli handler nell'ordine INFO -> WARNING -> ERROR."""
    # TODO: istanziare i tre handler e collegarli
    raise NotImplementedError("Completare la configurazione della chain")
