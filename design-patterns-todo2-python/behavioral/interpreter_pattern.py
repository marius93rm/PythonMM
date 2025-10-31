"""Pattern Interpreter
======================
Cos'è il pattern:
    L'Interpreter rappresenta una grammatica con oggetti e ne valuta le espressioni.
Obiettivo didattico:
    Implementare un piccolo linguaggio booleano con operatori AND, OR e NOT.
Scenario proposto:
    Le espressioni sono costruite come alberi e valutate a partire da un contesto di variabili.
Cosa deve fare lo studente:
    Definire le classi per variabili e operatori, completando il metodo `interpret` in ciascuna.
Passi TODO:
    1. Creare l'interfaccia `BooleanExpr` con `interpret(context)`.
    2. Implementare `VarExpr`, `NotExpr`, `AndExpr`, `OrExpr`.
    3. Scrivere una funzione di utility che costruisca un albero di esempio.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


class BooleanExpr(ABC):
    """Interfaccia per tutte le espressioni booleane."""

    # TODO: dichiarare metodo astratto interpret(context: dict[str, bool]) -> bool


@dataclass
class VarExpr(BooleanExpr):
    """Variabile booleana letta dal contesto."""

    name: str

    def interpret(self, context: Dict[str, bool]) -> bool:
        # TODO: restituire il valore corrispondente dal contesto
        raise NotImplementedError("Implementare interpret per VarExpr")


@dataclass
class NotExpr(BooleanExpr):
    """Negazione logica."""

    operand: BooleanExpr

    def interpret(self, context: Dict[str, bool]) -> bool:
        # TODO: negare il risultato dell'operando
        raise NotImplementedError("Implementare interpret per NotExpr")


@dataclass
class AndExpr(BooleanExpr):
    """Operatore logico AND."""

    left: BooleanExpr
    right: BooleanExpr

    def interpret(self, context: Dict[str, bool]) -> bool:
        # TODO: valutare left e right con AND logico
        raise NotImplementedError("Implementare interpret per AndExpr")


@dataclass
class OrExpr(BooleanExpr):
    """Operatore logico OR."""

    left: BooleanExpr
    right: BooleanExpr

    def interpret(self, context: Dict[str, bool]) -> bool:
        # TODO: valutare left e right con OR logico
        raise NotImplementedError("Implementare interpret per OrExpr")


def build_demo_expression() -> BooleanExpr:
    """Costruisce un albero di esempio per i test manuali."""
    # TODO: creare un'espressione composta (es. (A AND NOT B) OR C)
    raise NotImplementedError("Costruire un'espressione di esempio")
