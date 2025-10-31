"""Soluzione commentata del pattern Builder per Meal."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Meal:
    """Prodotto finale costruito dal builder."""

    main: Optional[str] = None
    side: Optional[str] = None
    drink: Optional[str] = None

    def describe(self) -> str:
        """Restituisce una descrizione leggibile del pasto."""
        return f"Meal(main={self.main}, side={self.side}, drink={self.drink})"


class MealBuilder:
    """Costruisce un `Meal` con un'interfaccia fluente."""

    def __init__(self) -> None:
        self._main: Optional[str] = None
        self._side: Optional[str] = None
        self._drink: Optional[str] = None

    def add_main(self, item: str) -> "MealBuilder":
        """Imposta il piatto principale."""
        self._main = item
        return self  # chaining fluente

    def add_side(self, item: str) -> "MealBuilder":
        """Imposta il contorno."""
        self._side = item
        return self

    def add_drink(self, item: str) -> "MealBuilder":
        """Imposta la bevanda."""
        self._drink = item
        return self

    def build(self) -> Meal:
        """Restituisce il `Meal` configurato."""
        # Creiamo un dataclass immutabile per evitare modifiche accidentali al risultato.
        meal = Meal(main=self._main, side=self._side, drink=self._drink)
        return meal


def prepare_combo(builder: MealBuilder) -> Meal:
    """Funzione di esempio che sfrutta il builder per creare un pasto standard."""
    # Esempio di combo tipo menù fast-food.
    return (
        builder.add_main("Burger")
        .add_side("Fries")
        .add_drink("Cola")
        .build()
    )
