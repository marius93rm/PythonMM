"""Soluzione commentata del pattern Memento."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class EditorMemento:
    """Rappresenta lo snapshot del testo."""

    content: str


class TextEditor:
    """Originator che genera memento dal proprio stato."""

    def __init__(self) -> None:
        self._content: str = ""

    def type_text(self, text: str) -> None:
        self._content += text

    def create_memento(self) -> EditorMemento:
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento) -> None:
        self._content = memento.content

    @property
    def content(self) -> str:
        return self._content


class HistoryCaretaker:
    """Gestisce la pila di memento."""

    def __init__(self) -> None:
        self._history: List[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        self._history.append(memento)

    def pop(self) -> EditorMemento:
        if not self._history:
            raise IndexError("History is empty")
        return self._history.pop()


def demo_editor() -> TextEditor:
    """Restituisce un editor da usare nei test manuali."""
    return TextEditor()
