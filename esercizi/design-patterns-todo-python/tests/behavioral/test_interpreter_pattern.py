import pytest

from behavioral.interpreter_pattern import (
    AndExpr,
    BooleanExpr,
    NotExpr,
    OrExpr,
    VarExpr,
    build_demo_expression,
)


@pytest.fixture()
def sample_context() -> dict[str, bool]:
    return {"A": True, "B": False, "C": False}


def test_var_expr_reads_value_from_context(sample_context: dict[str, bool]) -> None:
    expr = VarExpr("A")
    assert expr.interpret(sample_context) is True


def test_composite_expression_evaluates_logic(sample_context: dict[str, bool]) -> None:
    expression = AndExpr(VarExpr("A"), NotExpr(VarExpr("B")))
    assert expression.interpret(sample_context) is True


def test_or_expression_combines_branches(sample_context: dict[str, bool]) -> None:
    expression = OrExpr(NotExpr(VarExpr("A")), VarExpr("C"))
    assert expression.interpret(sample_context) is False


def test_demo_expression_matches_documentation() -> None:
    expression = build_demo_expression()
    assert isinstance(expression, BooleanExpr)

    assert expression.interpret({"A": True, "B": False, "C": False}) is True
    assert expression.interpret({"A": False, "B": False, "C": False}) is False
    assert expression.interpret({"A": False, "B": True, "C": True}) is True
