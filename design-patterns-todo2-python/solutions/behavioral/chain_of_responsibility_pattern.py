"""Soluzione commentata del pattern Chain of Responsibility."""

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
        if self._can_handle(message):
            self._process(message)
        elif self._next is not None:
            self._next.handle(message)
        else:
            print(f"[UNHANDLED] {message.level}: {message.text}")

    @abstractmethod
    def _can_handle(self, message: LogMessage) -> bool:
        """Determina se l'handler gestisce il messaggio."""

    @abstractmethod
    def _process(self, message: LogMessage) -> None:
        """Contiene la logica specifica del livello di log."""


class InfoLogHandler(LogHandler):
    """Gestisce i messaggi di livello INFO."""

    def _can_handle(self, message: LogMessage) -> bool:
        return message.level.upper() == "INFO"

    def _process(self, message: LogMessage) -> None:
        print(f"[INFO] {message.text}")


class WarningLogHandler(LogHandler):
    """Gestisce i messaggi di livello WARNING."""

    def _can_handle(self, message: LogMessage) -> bool:
        return message.level.upper() == "WARNING"

    def _process(self, message: LogMessage) -> None:
        print(f"[WARNING] {message.text}")


class ErrorLogHandler(LogHandler):
    """Gestisce i messaggi di livello ERROR."""

    def _can_handle(self, message: LogMessage) -> bool:
        return message.level.upper() == "ERROR"

    def _process(self, message: LogMessage) -> None:
        print(f"[ERROR] {message.text}")


def build_logging_chain() -> LogHandler:
    """Crea e collega gli handler nell'ordine INFO -> WARNING -> ERROR."""
    info = InfoLogHandler()
    warning = WarningLogHandler()
    error = ErrorLogHandler()
    info.set_next(warning).set_next(error)
    return info
