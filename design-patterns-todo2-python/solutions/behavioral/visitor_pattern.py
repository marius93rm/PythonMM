"""Soluzione commentata del pattern Visitor."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class ASTNode(ABC):
    """Nodo base dell'albero sintattico."""

    @abstractmethod
    def accept(self, visitor: "ASTVisitor") -> None:
        """Accetta un visitor esterno."""


@dataclass
class NumberNode(ASTNode):
    """Nodo che rappresenta un valore numerico."""

    value: int

    def accept(self, visitor: "ASTVisitor") -> None:
        visitor.visit_number(self)


@dataclass
class AddNode(ASTNode):
    """Nodo che rappresenta una somma."""

    left: ASTNode
    right: ASTNode

    def accept(self, visitor: "ASTVisitor") -> None:
        visitor.visit_add(self)


class ASTVisitor(ABC):
    """Visitor astratto per l'AST."""

    @abstractmethod
    def visit_number(self, node: NumberNode) -> None:
        ...

    @abstractmethod
    def visit_add(self, node: AddNode) -> None:
        ...


class EvaluationVisitor(ASTVisitor):
    """Calcola il valore dell'espressione."""

    def __init__(self) -> None:
        self.result: int | None = None

    def visit_number(self, node: NumberNode) -> None:
        self.result = node.value

    def visit_add(self, node: AddNode) -> None:
        node.left.accept(self)
        left_value = self.result or 0
        node.right.accept(self)
        right_value = self.result or 0
        self.result = left_value + right_value


class PrintVisitor(ASTVisitor):
    """Genera una rappresentazione testuale dell'espressione."""

    def __init__(self) -> None:
        self.output: str | None = None

    def visit_number(self, node: NumberNode) -> None:
        self.output = str(node.value)

    def visit_add(self, node: AddNode) -> None:
        node.left.accept(self)
        left_repr = self.output or ""
        node.right.accept(self)
        right_repr = self.output or ""
        self.output = f"({left_repr} + {right_repr})"


def build_expression_tree() -> ASTNode:
    """Crea un albero di esempio da utilizzare nei test manuali."""
    return AddNode(NumberNode(2), AddNode(NumberNode(3), NumberNode(4)))
