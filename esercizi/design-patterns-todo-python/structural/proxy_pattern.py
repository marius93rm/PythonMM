"""Pattern Proxy
================
Cos'è il pattern:
    Il Proxy controlla l'accesso a un oggetto reale, aggiungendo logica extra come lazy loading o caching.
Obiettivo didattico:
    Comprendere come differire la creazione di oggetti costosi fino a quando non servono davvero.
Scenario proposto:
    Una `RealImage` carica un file pesante solo quando bisogna mostrarlo, mentre `ProxyImage` rimanda l'operazione.
Cosa deve fare lo studente:
    Implementare l'interfaccia comune `Image` e completare le classi concreta e proxy.
Passi TODO:
    1. Definire il metodo `display()` nell'interfaccia `Image`.
    2. Simulare il caricamento pesante in `RealImage`.
    3. Implementare `ProxyImage` per istanziare `RealImage` solo alla prima richiesta.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Image(ABC):
    """Interfaccia comune per tutte le immagini."""

    # TODO: dichiarare metodo astratto display() -> str


class RealImage(Image):
    """Immagine che simula un caricamento pesante."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        # TODO: simulare caricamento oneroso (es. impostare un flag o chiamare un helper)

    def display(self) -> str:
        # TODO: restituire una stringa che indichi la visualizzazione dell'immagine
        raise NotImplementedError("Implementare display per RealImage")


class ProxyImage(Image):
    """Proxy che differisce la creazione della RealImage."""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self._real_image: Optional[RealImage] = None

    def display(self) -> str:
        # TODO: creare RealImage alla prima chiamata e delegare il display
        raise NotImplementedError("Implementare display con lazy loading")


def load_gallery(images: list[Image]) -> list[str]:
    """Esegue la visualizzazione di una serie di immagini."""
    result: list[str] = []
    for image in images:
        # TODO: chiamare display su ogni immagine e accumulare i risultati
        raise NotImplementedError("Completare la visualizzazione della galleria")
    return result
