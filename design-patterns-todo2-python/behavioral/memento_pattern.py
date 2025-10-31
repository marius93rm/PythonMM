"""Pattern Memento
==================
Cos'è il pattern:
    Il Memento salva e ripristina lo stato interno di un oggetto senza esporre i dettagli.
Obiettivo didattico:
    Implementare undo su un editor di testo usando Memento, Originator e Caretaker.
Scenario proposto:
    Un `TextEditor` scrive testo e può tornare a stati precedenti tramite una history di memento.
Cosa deve fare lo studente:
    Creare le classi necessarie e collegarle per gestire salvataggi e ripristini.
Passi TODO:
    1. Implementare `EditorMemento` per contenere lo stato del testo.
    2. Completare `TextEditor` con metodi per creare e ripristinare memento.
    3. Scrivere `HistoryCaretaker` che tiene traccia della cronologia.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class EditorMemento:
    """Rappresenta lo snapshot del testo."""

    # TODO: salvare il contenuto testuale


class TextEditor:
    """Originator che genera memento dal proprio stato."""

    def __init__(self) -> None:
        self._content: str = ""

    def type_text(self, text: str) -> None:
        self._content += text

    def create_memento(self) -> EditorMemento:
        # TODO: restituire un nuovo memento con lo stato attuale
        raise NotImplementedError("Creazione memento non implementata")

    def restore(self, memento: EditorMemento) -> None:
        # TODO: ripristinare lo stato dal memento
        raise NotImplementedError("Ripristino da memento non implementato")

    @property
    def content(self) -> str:
        return self._content


class HistoryCaretaker:
    """Gestisce la pila di memento."""

    def __init__(self) -> None:
        self._history: List[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        # TODO: aggiungere il memento alla history
        raise NotImplementedError("Push della history non implementato")

    def pop(self) -> EditorMemento:
        # TODO: estrarre l'ultimo memento e gestire il caso di history vuota
        raise NotImplementedError("Pop della history non implementato")


def demo_editor() -> TextEditor:
    """Restituisce un editor da usare nei test manuali."""
    editor = TextEditor()
    # TODO: eventualmente pre-caricare del testo o lasciare vuoto per esercizio
    return editor
