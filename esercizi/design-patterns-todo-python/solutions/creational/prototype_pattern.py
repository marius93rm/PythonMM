"""Soluzione commentata del pattern Prototype."""

from __future__ import annotations

import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    """Interfaccia base per oggetti clonabili."""

    @abstractmethod
    def clone(self) -> "Prototype":
        """Restituisce una copia indipendente dell'oggetto corrente."""


class Shape(Prototype):
    """Forma geometrica generica."""

    def __init__(self, color: str) -> None:
        self.color = color

    def clone(self) -> "Shape":
        """Clona l'oggetto corrente."""
        # copy.deepcopy assicura la duplicazione di tutto lo stato mutabile.
        return copy.deepcopy(self)


class Circle(Shape):
    """Implementazione concreta di Shape."""

    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def clone(self) -> "Circle":
        """Restituisce una nuova istanza di Circle con gli stessi valori."""
        return copy.deepcopy(self)


def clone_and_shift(shape: Shape, *, color: str | None = None) -> Shape:
    """Esempio di funzione che clona la shape e ne modifica eventuali attributi."""
    cloned = shape.clone()
    if color is not None:
        cloned.color = color  # type: ignore[assignment]
    return cloned
