"""Pattern Composite
====================
Cos'è il pattern:
    Il Composite unifica il trattamento di oggetti singoli e aggregati in una gerarchia ad albero.
Obiettivo didattico:
    Modellare strutture ricorsive come filesystem, sommando valori dai figli.
Scenario proposto:
    Stiamo costruendo una rappresentazione di cartelle e file con metodo `get_size()`.
Cosa deve fare lo studente:
    Definire l'interfaccia comune e implementare nodi foglia e composite che aggregano i figli.
Passi TODO:
    1. Creare la classe astratta `FileSystemNode` con `get_size()` e `describe()`.
    2. Implementare `FileNode` come foglia con dimensione fissa.
    3. Completare `DirectoryNode` gestendo la collezione di figli e il calcolo ricorsivo.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, List


class FileSystemNode(ABC):
    """Nodo generico di un filesystem virtuale."""

    # TODO: definire metodo astratto get_size() -> int
    # TODO: definire metodo astratto describe(indent: int = 0) -> str per rappresentazioni testuali


class FileNode(FileSystemNode):
    """Nodo foglia che rappresenta un file."""

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_size(self) -> int:
        # TODO: restituire la dimensione del file
        raise NotImplementedError("Implementare get_size per FileNode")

    def describe(self, indent: int = 0) -> str:
        # TODO: restituire una stringa descrittiva con indentazione
        raise NotImplementedError("Implementare describe per FileNode")


class DirectoryNode(FileSystemNode):
    """Nodo composto che contiene altri FileSystemNode."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[FileSystemNode] = []

    def add_child(self, child: FileSystemNode) -> None:
        # TODO: aggiungere il nodo figlio alla collezione interna
        raise NotImplementedError("Implementare add_child per DirectoryNode")

    def get_size(self) -> int:
        # TODO: sommare ricorsivamente le dimensioni dei figli
        raise NotImplementedError("Calcolo della dimensione composita non implementato")

    def describe(self, indent: int = 0) -> str:
        # TODO: restituire una stringa multi-linea con l'albero dei figli
        raise NotImplementedError("Implementare describe per DirectoryNode")


def build_sample_tree() -> DirectoryNode:
    """Costruisce un albero di esempio per test manuali."""
    # TODO: creare cartelle e file di esempio collegandoli tra loro
    raise NotImplementedError("Creare un albero di esempio per il composite")
