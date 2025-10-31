"""Soluzione commentata del pattern Command."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Command(ABC):
    """Interfaccia dei comandi dell'editor."""

    @abstractmethod
    def execute(self) -> None:
        """Esegue l'azione incapsulata."""


@dataclass
class TextDocument:
    """Ricevitore che mantiene il contenuto testuale."""

    content: str = ""

    def append(self, text: str) -> None:
        self.content += text

    def clear(self) -> None:
        self.content = ""


class AppendTextCommand(Command):
    """Aggiunge testo al documento."""

    def __init__(self, document: TextDocument, text: str) -> None:
        self.document = document
        self.text = text

    def execute(self) -> None:
        self.document.append(self.text)


class ClearTextCommand(Command):
    """Cancella il contenuto del documento."""

    def __init__(self, document: TextDocument) -> None:
        self.document = document

    def execute(self) -> None:
        self.document.clear()


class EditorInvoker:
    """Invoca i comandi e mantiene la history."""

    def __init__(self) -> None:
        self.history: List[Command] = []

    def run(self, command: Command) -> None:
        command.execute()
        self.history.append(command)

    def last_commands(self) -> List[Command]:
        """Restituisce la history attuale."""
        return list(self.history)


def setup_editor() -> tuple[TextDocument, EditorInvoker]:
    """Restituisce un documento e un invoker pronti per essere usati nei test manuali."""
    document = TextDocument()
    invoker = EditorInvoker()
    return document, invoker
