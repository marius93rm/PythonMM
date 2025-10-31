"""Soluzione commentata del pattern Flyweight."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class IconFlyweight:
    """Rappresenta l'icona condivisa con stato intrinseco."""

    shape: str
    color: str

    def render(self, x: int, y: int) -> str:
        """Restituisce una descrizione della renderizzazione."""
        return f"Render {self.shape}/{self.color} at ({x}, {y})"


class IconFactory:
    """Gestisce la cache degli icon flyweight."""

    def __init__(self) -> None:
        self._cache: Dict[Tuple[str, str], IconFlyweight] = {}

    def get_icon(self, shape: str, color: str) -> IconFlyweight:
        """Restituisce un flyweight condiviso per la coppia shape/color."""
        key = (shape, color)
        if key not in self._cache:
            self._cache[key] = IconFlyweight(shape=shape, color=color)
        return self._cache[key]


def render_map(factory: IconFactory, points: list[tuple[str, str, tuple[int, int]]]) -> list[str]:
    """Esempio che mostra come usare stato estrinseco con il flyweight."""
    rendered: list[str] = []
    for shape, color, position in points:
        icon = factory.get_icon(shape, color)
        x, y = position
        rendered.append(icon.render(x, y))
    return rendered
