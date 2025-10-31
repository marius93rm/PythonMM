"""Soluzione commentata del pattern Proxy."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Image(ABC):
    """Interfaccia comune per tutte le immagini."""

    @abstractmethod
    def display(self) -> str:
        """Visualizza l'immagine (o simula la visualizzazione)."""


class RealImage(Image):
    """Immagine che simula un caricamento pesante."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self._loaded = False
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        # Simuliamo un'operazione costosa che avviene soltanto per l'immagine reale.
        print(f"Loading {self.file_path} from disk...")
        self._loaded = True

    def display(self) -> str:
        message = f"Displaying {self.file_path}"
        print(message)
        return message


class ProxyImage(Image):
    """Proxy che differisce la creazione della RealImage."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self._real_image: Optional[RealImage] = None

    def display(self) -> str:
        if self._real_image is None:
            print("Lazy loading real image...")
            self._real_image = RealImage(self.file_path)
        return self._real_image.display()


def load_gallery(images: list[Image]) -> list[str]:
    """Esegue la visualizzazione di una serie di immagini."""
    result: list[str] = []
    for image in images:
        result.append(image.display())
    return result
