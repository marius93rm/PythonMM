"""Pattern Flyweight
====================
Cos'è il pattern:
    Il Flyweight condivide oggetti leggeri per ridurre l'utilizzo di memoria in presenza di molti elementi simili.
Obiettivo didattico:
    Distinguere tra stato condiviso (intrinseco) e stato contestuale (estrinseco).
Scenario proposto:
    Gestiamo icone grafiche per una mappa, riutilizzando oggetti con la stessa forma e colore.
Cosa deve fare lo studente:
    Implementare la factory che mantiene una cache di `IconFlyweight` e fornisce istanze riutilizzate.
Passi TODO:
    1. Definire la classe `IconFlyweight` con stato intrinseco (forma, colore).
    2. Creare `IconFactory` con cache interna e metodo `get_icon`.
    3. Mostrare nel metodo demo come lo stato estrinseco (es. posizione) è gestito fuori dal flyweight.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class IconFlyweight:
    """Rappresenta l'icona condivisa con stato intrinseco."""

    # TODO: aggiungere campi shape e color

    def render(self, x: int, y: int) -> str:
        """Restituisce una descrizione della renderizzazione."""
        # TODO: utilizzare shape e color per creare la descrizione
        raise NotImplementedError("Completare render per IconFlyweight")


class IconFactory:
    """Gestisce la cache degli icon flyweight."""

    def __init__(self) -> None:
        self._cache: Dict[Tuple[str, str], IconFlyweight] = {}

    def get_icon(self, shape: str, color: str) -> IconFlyweight:
        """Restituisce un flyweight condiviso per la coppia shape/color."""
        # TODO: restituire dalla cache se disponibile, altrimenti creare e salvare
        raise NotImplementedError("Implementare la gestione della cache di flyweight")


def render_map(factory: IconFactory, points: list[tuple[str, str, tuple[int, int]]]) -> list[str]:
    """Esempio che mostra come usare stato estrinseco con il flyweight."""
    rendered: list[str] = []
    for shape, color, position in points:
        # TODO: ottenere il flyweight dalla factory e chiamare render con la posizione
        raise NotImplementedError("Completare il ciclo di renderizzazione della mappa")
    return rendered
