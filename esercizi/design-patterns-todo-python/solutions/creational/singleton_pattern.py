"""Soluzione del pattern Singleton per AppConfig.

Questo file replica l'esercizio originale sostituendo i TODO con un'implementazione
completa e qualche commento esplicativo per ripassare i passaggi chiave.
"""

from __future__ import annotations

from typing import Any


class AppConfig:
    """Configurazione globale con semantica Singleton."""

    _instance: "AppConfig | None" = None
    _initialized: bool = False

    def __new__(cls, *args: Any, **kwargs: Any) -> "AppConfig":
        # Creiamo l'istanza solo la prima volta; le chiamate successive riusano la stessa.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, app_name: str, debug: bool = False) -> None:
        if self.__class__._initialized:
            return
        # Persistiamo i valori solo durante la prima inizializzazione.
        self._app_name = app_name
        self._debug = debug
        self.__class__._initialized = True

    @property
    def app_name(self) -> str:
        """Nome leggibile dell'applicazione."""
        return self._app_name

    @property
    def debug(self) -> bool:
        """Indica se il sistema è in modalità debug."""
        return self._debug


def get_app_config() -> AppConfig:
    """Helper per accedere all'istanza condivisa."""

    # Se non esiste ancora, creiamo una configurazione con valori di default.
    instance = AppConfig._instance
    if instance is None:
        instance = AppConfig("DefaultApp", debug=False)
    return instance
