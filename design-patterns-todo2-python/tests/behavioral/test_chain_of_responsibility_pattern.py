import pytest

from behavioral.chain_of_responsibility_pattern import (
    ErrorLogHandler,
    InfoLogHandler,
    LogMessage,
    WarningLogHandler,
    build_logging_chain,
)


def test_build_logging_chain_links_handlers_in_order() -> None:
    root = build_logging_chain()
    assert isinstance(root, InfoLogHandler)
    assert isinstance(root._next, WarningLogHandler)
    assert isinstance(root._next._next, ErrorLogHandler)


def test_chain_processes_each_log_level() -> None:
    chain = build_logging_chain()

    info_result = chain.handle(LogMessage(level="INFO", text="system ready"))
    warning_result = chain.handle(LogMessage(level="WARNING", text="temperature high"))
    error_result = chain.handle(LogMessage(level="ERROR", text="disk failure"))

    assert info_result == "INFO: system ready"
    assert warning_result == "WARNING: temperature high"
    assert error_result == "ERROR: disk failure"


def test_chain_returns_none_for_unknown_level() -> None:
    chain = build_logging_chain()
    assert chain.handle(LogMessage(level="DEBUG", text="verbose")) is None
