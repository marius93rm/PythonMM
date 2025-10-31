"""Soluzione commentata del pattern Strategy."""

from __future__ import annotations

from abc import ABC, abstractmethod


class TextFormatStrategy(ABC):
    """Contratto comune per le strategie di formattazione."""

    @abstractmethod
    def format(self, text: str) -> str:
        """Trasforma il testo secondo la strategia."""


class UpperCaseStrategy(TextFormatStrategy):
    """Trasforma il testo in maiuscolo."""

    def format(self, text: str) -> str:
        return text.upper()


class LowerCaseStrategy(TextFormatStrategy):
    """Trasforma il testo in minuscolo."""

    def format(self, text: str) -> str:
        return text.lower()


class TitleCaseStrategy(TextFormatStrategy):
    """Trasforma il testo in Title Case."""

    def format(self, text: str) -> str:
        return text.title()


class TextFormatter:
    """Contesto che usa una strategia di formattazione."""

    def __init__(self, strategy: TextFormatStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: TextFormatStrategy) -> None:
        self._strategy = strategy

    def format(self, text: str) -> str:
        return self._strategy.format(text)


def build_formatter() -> TextFormatter:
    """Helper che restituisce un formatter con strategia di default."""
    return TextFormatter(UpperCaseStrategy())
