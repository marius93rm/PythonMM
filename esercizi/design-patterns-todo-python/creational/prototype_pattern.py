"""Pattern Prototype
====================
Cos'è il pattern:
    Il Prototype crea nuove istanze clonando un oggetto esistente, evitando di invocare il costruttore.
Obiettivo didattico:
    Imparare a duplicare oggetti mantenendo l'indipendenza dello stato.
Scenario proposto:
    Una gerarchia di forme geometriche deve poter clonare i propri dati per generare copie modificate.
Cosa deve fare lo studente:
    Implementare il metodo `clone()` e gestire la copia profonda delle proprietà.
Passi TODO:
    1. Definire l'interfaccia `Prototype` con `clone()`.
    2. Completare la classe `Shape` e l'implementazione concreta `Circle`.
    3. Utilizzare una strategia di copia (es. `copy.deepcopy`) nei punti indicati.
"""

from __future__ import annotations

import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    """Interfaccia base per oggetti clonabili."""

    # TODO: dichiarare metodo astratto clone() -> "Prototype"


class Shape(Prototype):
    """Forma geometrica generica."""

    def __init__(self, color: str) -> None:
        self.color = color

    def clone(self) -> "Shape":
        """Clona l'oggetto corrente."""
        # TODO: restituire una copia dell'istanza corrente
        raise NotImplementedError("Implementare la logica di clone di Shape")


class Circle(Shape):
    """Implementazione concreta di Shape."""

    def __init__(self, color: str, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def clone(self) -> "Circle":
        """Restituisce una nuova istanza di Circle con gli stessi valori."""
        # TODO: usare una copia profonda per duplicare l'oggetto
        raise NotImplementedError("Clonazione del cerchio non implementata")


def clone_and_shift(shape: Shape, *, color: str | None = None) -> Shape:
    """Esempio di funzione che clona la shape e ne modifica eventuali attributi."""
    # TODO: clonare la shape e applicare eventuali modifiche al colore
    raise NotImplementedError("Completare l'esempio di clonazione e modifica")
