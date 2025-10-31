from behavioral.visitor_pattern import (
    AddNode,
    EvaluationVisitor,
    NumberNode,
    PrintVisitor,
    build_expression_tree,
)


def test_number_node_accepts_visitor() -> None:
    node = NumberNode(5)
    visitor = EvaluationVisitor()
    node.accept(visitor)
    assert visitor.result == 5


def test_evaluation_visitor_sums_children() -> None:
    tree = AddNode(NumberNode(2), AddNode(NumberNode(3), NumberNode(4)))
    visitor = EvaluationVisitor()
    tree.accept(visitor)
    assert visitor.result == 9


def test_print_visitor_generates_parenthesized_expression() -> None:
    tree = build_expression_tree()
    printer = PrintVisitor()
    tree.accept(printer)
    assert printer.output == "(1 + (2 + 3))"

    evaluator = EvaluationVisitor()
    tree.accept(evaluator)
    assert evaluator.result == 6
