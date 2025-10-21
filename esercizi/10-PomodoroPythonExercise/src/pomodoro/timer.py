from __future__ import annotations
from typing import Protocol, Callable
import time

class ITickProvider(Protocol):
    """Protocol per astrarre l'attesa di 1 secondo (o tick)."""
    def tick(self) -> None: ...

class RealTickProvider:
    """Implementazione reale: attende 1 secondo."""
    def tick(self) -> None:
        time.sleep(1)

class TimerService:
    """
    Responsabilità singola: scandire un countdown in secondi
    chiamando due callback: on_tick(int seconds_left) e on_completed().
    DIP: dipende da ITickProvider, iniettabile nei test.
    """
    def __init__(self, tick_provider: ITickProvider | None = None) -> None:
        self._tick = tick_provider or RealTickProvider()

    def countdown(self, seconds: int, *, on_tick: Callable[[int], None], on_completed: Callable[[], None]) -> None:
        """
        TODO M1:
        - Validare che `seconds` sia >= 0 (ValueError altrimenti).
        - Per ogni secondo rimanente, chiamare on_tick(seconds_left) e poi attendere un tick.
        - Al termine, chiamare on_completed().
        Note: per i test useremo un FakeTickProvider che non dorme davvero.
        Suggerimento: usa un loop decrescente.
        """
        # TODO: implementare la logica descritta sopra
        raise NotImplementedError("Implementa TimerService.countdown (Milestone 1)")
