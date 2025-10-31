"""Pattern Builder
==================
Cos'è il pattern:
    Il Builder costruisce oggetti complessi attraverso una sequenza di passi controllati.
Obiettivo didattico:
    Separare la costruzione dalla rappresentazione, offrendo un'API fluente.
Scenario proposto:
    Vogliamo comporre un pasto (`Meal`) indicando panino, contorno e bevanda con ordine flessibile.
Cosa deve fare lo studente:
    Definire la classe prodotto e completare il builder con metodi fluenti e `build()`.
Passi TODO:
    1. Creare la classe `Meal` con attributi per piatto principale, contorno e bevanda.
    2. Implementare i metodi del builder `add_main`, `add_side`, `add_drink` restituendo `self`.
    3. Far sì che `build()` restituisca una copia immutabile dello stato attuale del pasto.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Meal:
    """Prodotto finale costruito dal builder."""

    # TODO: definire i campi main, side e drink con tipi opzionali di str
    # Suggerimento: usa valori di default None e aggiungi eventuali metadati se utili.

    def describe(self) -> str:
        """Restituisce una descrizione leggibile del pasto."""
        main = getattr(self, "main", None)
        side = getattr(self, "side", None)
        drink = getattr(self, "drink", None)
        return f"Meal(main={main}, side={side}, drink={drink})"


class MealBuilder:
    """Costruisce un `Meal` con un'interfaccia fluente."""

    def __init__(self) -> None:
        self._main: Optional[str] = None
        self._side: Optional[str] = None
        self._drink: Optional[str] = None

    def add_main(self, item: str) -> "MealBuilder":
        """Imposta il piatto principale."""
        # TODO: salvare il piatto principale e restituire self per consentire chaining
        raise NotImplementedError("Implementare add_main")

    def add_side(self, item: str) -> "MealBuilder":
        """Imposta il contorno."""
        # TODO: salvare il contorno e restituire self
        raise NotImplementedError("Implementare add_side")

    def add_drink(self, item: str) -> "MealBuilder":
        """Imposta la bevanda."""
        # TODO: salvare la bevanda e restituire self
        raise NotImplementedError("Implementare add_drink")

    def build(self) -> Meal:
        """Restituisce il `Meal` configurato."""
        # TODO: creare un oggetto Meal con i campi raccolti
        # TODO: valutare se resettare lo stato interno o lasciare a carico del chiamante
        raise NotImplementedError("Costruzione del Meal non completata")


def prepare_combo(builder: MealBuilder) -> Meal:
    """Funzione di esempio che sfrutta il builder per creare un pasto standard."""
    # TODO: usare il builder per configurare una combinazione e restituire il risultato
    raise NotImplementedError("Implementare la preparazione di un combo")
