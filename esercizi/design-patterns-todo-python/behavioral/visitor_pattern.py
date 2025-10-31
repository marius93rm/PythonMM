"""Pattern Visitor
==================
Cos'è il pattern:
    Il Visitor separa un'operazione dalla struttura dati su cui opera, consentendo di aggiungere nuove operazioni senza modificare i nodi.
Obiettivo didattico:
    Costruire un piccolo AST aritmetico con visitor che calcolano il valore o stampano l'espressione.
Scenario proposto:
    Nodi `NumberNode` e `AddNode` espongono `accept(visitor)` per delegare la logica al visitor.
Cosa deve fare lo studente:
    Implementare le interfacce dei nodi e del visitor, completando i metodi chiave.
Passi TODO:
    1. Definire la classe base `ASTNode` con il metodo `accept`.
    2. Creare il visitor astratto con i metodi `visit_number` e `visit_add`.
    3. Implementare visitor concreti per valutare o stampare l'albero.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class ASTNode(ABC):
    """Nodo base dell'albero sintattico."""

    # TODO: dichiarare metodo astratto accept(visitor: "ASTVisitor") -> None


@dataclass
class NumberNode(ASTNode):
    """Nodo che rappresenta un valore numerico."""

    value: int

    def accept(self, visitor: "ASTVisitor") -> None:
        # TODO: delegare al metodo visit_number del visitor
        raise NotImplementedError("Implementare accept per NumberNode")


@dataclass
class AddNode(ASTNode):
    """Nodo che rappresenta una somma."""

    left: ASTNode
    right: ASTNode

    def accept(self, visitor: "ASTVisitor") -> None:
        # TODO: delegare al metodo visit_add del visitor
        raise NotImplementedError("Implementare accept per AddNode")


class ASTVisitor(ABC):
    """Visitor astratto per l'AST."""

    # TODO: dichiarare metodi astratti visit_number(node: NumberNode) e visit_add(node: AddNode)


class EvaluationVisitor(ASTVisitor):
    """Calcola il valore dell'espressione."""

    def __init__(self) -> None:
        self.result: int | None = None

    def visit_number(self, node: NumberNode) -> None:
        # TODO: impostare result con il valore del numero
        raise NotImplementedError("Implementare visit_number per EvaluationVisitor")

    def visit_add(self, node: AddNode) -> None:
        # TODO: visitare i figli e calcolare la somma
        raise NotImplementedError("Implementare visit_add per EvaluationVisitor")


class PrintVisitor(ASTVisitor):
    """Genera una rappresentazione testuale dell'espressione."""

    def __init__(self) -> None:
        self.output: str | None = None

    def visit_number(self, node: NumberNode) -> None:
        # TODO: aggiornare output con il valore del numero
        raise NotImplementedError("Implementare visit_number per PrintVisitor")

    def visit_add(self, node: AddNode) -> None:
        # TODO: visitare i figli e costruire una stringa formattata
        raise NotImplementedError("Implementare visit_add per PrintVisitor")


def build_expression_tree() -> ASTNode:
    """Crea un albero di esempio da utilizzare nei test manuali."""
    # TODO: costruire un AddNode con alcuni NumberNode
    raise NotImplementedError("Creare un albero di esempio per il visitor")
