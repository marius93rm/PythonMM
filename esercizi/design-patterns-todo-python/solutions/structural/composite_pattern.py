"""Soluzione commentata del pattern Composite."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, List


class FileSystemNode(ABC):
    """Nodo generico di un filesystem virtuale."""

    @abstractmethod
    def get_size(self) -> int:
        """Restituisce la dimensione complessiva del nodo."""

    @abstractmethod
    def describe(self, indent: int = 0) -> str:
        """Restituisce una rappresentazione testuale indentata."""


class FileNode(FileSystemNode):
    """Nodo foglia che rappresenta un file."""

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def describe(self, indent: int = 0) -> str:
        padding = " " * indent
        return f"{padding}- {self.name} ({self.size} KB)"


class DirectoryNode(FileSystemNode):
    """Nodo composto che contiene altri FileSystemNode."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[FileSystemNode] = []

    def add_child(self, child: FileSystemNode) -> None:
        self._children.append(child)

    def add_children(self, children: Iterable[FileSystemNode]) -> None:
        for child in children:
            self.add_child(child)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def describe(self, indent: int = 0) -> str:
        padding = " " * indent
        lines = [f"{padding}+ {self.name}/ ({self.get_size()} KB)"]
        for child in self._children:
            lines.append(child.describe(indent + 2))
        return "\n".join(lines)


def build_sample_tree() -> DirectoryNode:
    """Costruisce un albero di esempio per test manuali."""
    root = DirectoryNode("root")
    documents = DirectoryNode("documents")
    media = DirectoryNode("media")

    documents.add_children(
        [
            FileNode("cv.pdf", 120),
            FileNode("report.docx", 80),
        ]
    )
    media.add_children(
        [
            FileNode("song.mp3", 5120),
            FileNode("video.mp4", 20480),
        ]
    )
    root.add_children([documents, media, FileNode("notes.txt", 8)])
    return root
