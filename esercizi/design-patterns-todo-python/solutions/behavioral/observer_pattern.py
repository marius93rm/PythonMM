"""Soluzione commentata del pattern Observer."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


class Observer(ABC):
    """Interfaccia per gli osservatori."""

    @abstractmethod
    def update(self, temperature: float, humidity: float) -> None:
        """Riceve gli aggiornamenti dal soggetto osservato."""


class Subject(ABC):
    """Interfaccia per i soggetti osservabili."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        ...

    @abstractmethod
    def notify(self) -> None:
        ...


class WeatherStation(Subject):
    """Subject che mantiene i dati meteo."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def update_measurements(self, temperature: float, humidity: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self.notify()


@dataclass
class DisplayObserver(Observer):
    """Osservatore che visualizza i dati su un display."""

    name: str
    history: List[str] = field(default_factory=list)

    def update(self, temperature: float, humidity: float) -> None:
        message = f"{self.name} -> Temp: {temperature:.1f}°C, Humidity: {humidity:.1f}%"
        self.history.append(message)
        print(message)


def setup_weather_station() -> WeatherStation:
    """Utility per creare una stazione meteo pronta per i test manuali."""
    station = WeatherStation()
    return station
