from structural.decorator_pattern import (
    LoggingDataSource,
    SimpleDataSource,
    make_logging_source,
)


def test_simple_data_source_roundtrip() -> None:
    source = SimpleDataSource()
    source.write("design patterns")
    assert source.read() == "design patterns"


def test_logging_data_source_delegates_to_wrapped() -> None:
    inner = SimpleDataSource()
    logging_source = LoggingDataSource(inner)
    logging_source.write("observer")
    assert inner.read() == "observer"
    # La lettura deve delegare alla sorgente interna.
    assert logging_source.read() == "observer"


def test_make_logging_source_creates_wrapped_instance() -> None:
    wrapped = make_logging_source()
    assert isinstance(wrapped, LoggingDataSource)
    wrapped.write("strategy")
    assert wrapped.read() == "strategy"
