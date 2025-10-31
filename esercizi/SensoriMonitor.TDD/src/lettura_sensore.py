"""Modulo dedicato alla rappresentazione di una singola lettura del sensore.

La responsabilità di questa classe è semplice: incapsulare i valori raccolti da un
sensore IoT (temperatura, umidità e timestamp) in modo che possano essere testati.
Seguendo il principio SRP (Single Responsibility Principle), questa classe non deve
prendersi carico di altro.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any


class LetturaSensore:
    """Rappresenta una lettura atomica proveniente da un sensore.

    Nel percorso TDD, prima scriveremo i test (milestone 1) per descrivere come
    vogliamo che questa classe si comporti. Solo dopo implementeremo il minimo
    necessario per farli passare.
    """

    # TODO 1.1: definisci il costruttore salvando temperatura, umidità e timestamp.
    #           Valuta se salvare il timestamp come `datetime` o come stringa ISO.
    #           Ricorda che i test verificheranno che questi attributi siano in sola lettura.
    def __init__(self, temperatura: float, umidita: float, timestamp: Any) -> None:
        """Inizializza una lettura.

        Gli studenti dovranno decidere come memorizzare il timestamp durante la
        milestone 1. Si suggerisce di documentare eventuali decisioni nei test.
        """
        # Esempio di approccio possibile (da completare nei TODO):
        # self._temperatura = ...
        # self._umidita = ...
        # self._timestamp = ...
        raise NotImplementedError("Completa il TODO 1.1 prima di usare LetturaSensore")

    @property
    def temperatura(self) -> float:
        """Restituisce la temperatura registrata (proprietà in sola lettura)."""
        # TODO 1.1: restituisci il valore memorizzato nel costruttore.
        raise NotImplementedError

    @property
    def umidita(self) -> float:
        """Restituisce l'umidità registrata (proprietà in sola lettura)."""
        # TODO 1.1: restituisci il valore memorizzato nel costruttore.
        raise NotImplementedError

    @property
    def timestamp(self) -> Any:
        """Restituisce il timestamp della lettura (formato deciso nei test)."""
        # TODO 1.1: restituisci il valore memorizzato nel costruttore.
        raise NotImplementedError

    def __repr__(self) -> str:
        """Rappresentazione utile per il debug durante i test."""
        return (
            "LetturaSensore(temperatura="
            f"{getattr(self, '_temperatura', '?')}, umidita={getattr(self, '_umidita', '?')}, "
            f"timestamp={getattr(self, '_timestamp', '?')})"
        )
