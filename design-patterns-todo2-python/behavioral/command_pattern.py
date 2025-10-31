"""Pattern Command
==================
Cos'è il pattern:
    Il Command incapsula un'azione e il suo ricevitore in un oggetto invocabile.
Obiettivo didattico:
    Separare le azioni dall'invoker e mantenere una history.
Scenario proposto:
    Un editor testuale deve eseguire comandi di append e clear mantenendo lo stato.
Cosa deve fare lo studente:
    Implementare i comandi concreti e completare l'invoker con gestione della history.
Passi TODO:
    1. Definire l'interfaccia `Command` con il metodo `execute()`.
    2. Implementare `AppendTextCommand` e `ClearTextCommand` applicando le modifiche all'editor.
    3. Aggiornare `EditorInvoker` per registrare i comandi eseguiti.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Command(ABC):
    """Interfaccia dei comandi dell'editor."""

    # TODO: dichiarare metodo astratto execute() -> None


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
        # TODO: delegare a document.append
        raise NotImplementedError("Implementare l'append nel comando")


class ClearTextCommand(Command):
    """Cancella il contenuto del documento."""

    def __init__(self, document: TextDocument) -> None:
        self.document = document

    def execute(self) -> None:
        # TODO: delegare a document.clear
        raise NotImplementedError("Implementare il clear nel comando")


class EditorInvoker:
    """Invoca i comandi e mantiene la history."""

    def __init__(self) -> None:
        self.history: List[Command] = []

    def run(self, command: Command) -> None:
        # TODO: eseguire il comando e salvarlo nella history
        raise NotImplementedError("Completare l'esecuzione del comando")

    def last_commands(self) -> List[Command]:
        """Restituisce la history attuale."""
        return list(self.history)


def setup_editor() -> tuple[TextDocument, EditorInvoker]:
    """Restituisce un documento e un invoker pronti per essere usati nei test manuali."""
    document = TextDocument()
    invoker = EditorInvoker()
    # TODO: eventualmente predisporre comandi di esempio o lasciare ai test manuali
    return document, invoker
