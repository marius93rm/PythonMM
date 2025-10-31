"""Pattern Strategy
===================
Cos'è il pattern:
    Lo Strategy incapsula algoritmi intercambiabili all'interno di oggetti riutilizzabili.
Obiettivo didattico:
    Implementare formattatori di testo con strategie differenti.
Scenario proposto:
    `TextFormatter` può trasformare stringhe in maiuscolo, minuscolo o title case a runtime.
Cosa deve fare lo studente:
    Definire le strategie concrete e consentire il cambio dinamico della strategia.
Passi TODO:
    1. Creare l'interfaccia `TextFormatStrategy` con il metodo `format(text)`.
    2. Implementare `UpperCaseStrategy`, `LowerCaseStrategy`, `TitleCaseStrategy`.
    3. Completare `TextFormatter` con `set_strategy` e `format` che delegano alla strategia corrente.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class TextFormatStrategy(ABC):
    """Contratto comune per le strategie di formattazione."""

    # TODO: dichiarare metodo astratto format(text: str) -> str


class UpperCaseStrategy(TextFormatStrategy):
    """Trasforma il testo in maiuscolo."""

    def format(self, text: str) -> str:
        # TODO: restituire il testo trasformato
        raise NotImplementedError("Implementare UpperCaseStrategy")


class LowerCaseStrategy(TextFormatStrategy):
    """Trasforma il testo in minuscolo."""

    def format(self, text: str) -> str:
        # TODO: restituire il testo trasformato
        raise NotImplementedError("Implementare LowerCaseStrategy")


class TitleCaseStrategy(TextFormatStrategy):
    """Trasforma il testo in Title Case."""

    def format(self, text: str) -> str:
        # TODO: restituire il testo con iniziali maiuscole
        raise NotImplementedError("Implementare TitleCaseStrategy")


class TextFormatter:
    """Contesto che usa una strategia di formattazione."""

    def __init__(self, strategy: TextFormatStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: TextFormatStrategy) -> None:
        # TODO: aggiornare la strategia corrente
        raise NotImplementedError("Implementare set_strategy")

    def format(self, text: str) -> str:
        # TODO: delegare il lavoro alla strategia corrente
        raise NotImplementedError("Delegare alla strategia")


def build_formatter() -> TextFormatter:
    """Helper che restituisce un formatter con strategia di default."""
    # TODO: restituire un TextFormatter configurato con una strategia iniziale
    raise NotImplementedError("Creare un formatter di esempio")
