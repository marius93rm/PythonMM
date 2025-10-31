import pytest

from behavioral.strategy_pattern import (
    LowerCaseStrategy,
    TextFormatStrategy,
    TextFormatter,
    TitleCaseStrategy,
    UpperCaseStrategy,
    build_formatter,
)


@pytest.fixture()
def sample_text() -> str:
    return "pattern strategy"


def test_build_formatter_returns_formatter(sample_text: str) -> None:
    formatter = build_formatter()
    assert isinstance(formatter, TextFormatter)
    # Il formatter di default deve essere pronto a formattare il testo.
    assert formatter.format(sample_text) == sample_text.upper()


@pytest.mark.parametrize(
    "strategy,expected",
    [
        (UpperCaseStrategy(), "PATTERN STRATEGY"),
        (LowerCaseStrategy(), "pattern strategy"),
        (TitleCaseStrategy(), "Pattern Strategy"),
    ],
)
def test_formatter_switches_strategy(
    strategy: TextFormatStrategy, expected: str, sample_text: str
) -> None:
    formatter = build_formatter()
    formatter.set_strategy(strategy)
    assert formatter.format(sample_text) == expected
