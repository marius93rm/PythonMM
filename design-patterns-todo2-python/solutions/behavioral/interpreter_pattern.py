"""Soluzione commentata del pattern Interpreter."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


class BooleanExpr(ABC):
    """Interfaccia per tutte le espressioni booleane."""

    @abstractmethod
    def interpret(self, context: Dict[str, bool]) -> bool:
        """Valuta l'espressione usando il contesto fornito."""


@dataclass
class VarExpr(BooleanExpr):
    """Variabile booleana letta dal contesto."""

    name: str

    def interpret(self, context: Dict[str, bool]) -> bool:
        return context[self.name]


@dataclass
class NotExpr(BooleanExpr):
    """Negazione logica."""

    operand: BooleanExpr

    def interpret(self, context: Dict[str, bool]) -> bool:
        return not self.operand.interpret(context)


@dataclass
class AndExpr(BooleanExpr):
    """Operatore logico AND."""

    left: BooleanExpr
    right: BooleanExpr

    def interpret(self, context: Dict[str, bool]) -> bool:
        return self.left.interpret(context) and self.right.interpret(context)


@dataclass
class OrExpr(BooleanExpr):
    """Operatore logico OR."""

    left: BooleanExpr
    right: BooleanExpr

    def interpret(self, context: Dict[str, bool]) -> bool:
        return self.left.interpret(context) or self.right.interpret(context)


def build_demo_expression() -> BooleanExpr:
    """Costruisce un albero di esempio per i test manuali."""
    # (A AND NOT B) OR C
    return OrExpr(
        AndExpr(VarExpr("A"), NotExpr(VarExpr("B"))),
        VarExpr("C"),
    )
