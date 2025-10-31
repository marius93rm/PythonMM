"""Pattern Observer
===================
Cos'è il pattern:
    L'Observer permette a un soggetto di notificare automaticamente più osservatori quando cambia stato.
Obiettivo didattico:
    Implementare un sistema meteo che aggiorna display multipli.
Scenario proposto:
    `WeatherStation` pubblica aggiornamenti su temperatura e umidità agli osservatori registrati.
Cosa deve fare lo studente:
    Definire le interfacce e gestire la registrazione, la rimozione e le notifiche.
Passi TODO:
    1. Creare le interfacce `Observer` e `Subject` con i metodi necessari.
    2. Implementare `WeatherStation` con gestione degli osservatori.
    3. Realizzare `DisplayObserver` che reagisce agli aggiornamenti.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Observer(ABC):
    """Interfaccia per gli osservatori."""

    # TODO: dichiarare metodo astratto update(temperature: float, humidity: float) -> None


class Subject(ABC):
    """Interfaccia per i soggetti osservabili."""

    # TODO: dichiarare metodi astratti attach(observer), detach(observer), notify()


class WeatherStation(Subject):
    """Subject che mantiene i dati meteo."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0

    def attach(self, observer: Observer) -> None:
        # TODO: aggiungere un osservatore
        raise NotImplementedError("Implementare attach")

    def detach(self, observer: Observer) -> None:
        # TODO: rimuovere un osservatore
        raise NotImplementedError("Implementare detach")

    def notify(self) -> None:
        # TODO: notificare tutti gli osservatori con temperatura e umidità correnti
        raise NotImplementedError("Implementare notify")

    def update_measurements(self, temperature: float, humidity: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        # TODO: invocare notify dopo l'aggiornamento
        raise NotImplementedError("Richiamare notify dopo aggiornamento")


@dataclass
class DisplayObserver(Observer):
    """Osservatore che visualizza i dati su un display."""

    name: str

    def update(self, temperature: float, humidity: float) -> None:
        # TODO: memorizzare o mostrare i dati aggiornati (anche con una semplice print)
        raise NotImplementedError("Implementare update del display")


def setup_weather_station() -> WeatherStation:
    """Utility per creare una stazione meteo pronta per i test manuali."""
    station = WeatherStation()
    # TODO: facoltativamente aggiungere osservatori demo
    return station
