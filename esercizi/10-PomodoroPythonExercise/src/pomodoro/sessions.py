from __future__ import annotations
from typing import Protocol, Tuple

class ISessionStrategy(Protocol):
    def get_durations(self) -> Tuple[int, int]:
        """Ritorna (focus_seconds, break_seconds)."""
        ...

class Classic25_5:
    def get_durations(self) -> Tuple[int, int]:
        return 25*60, 5*60

class Deep50_10:
    def get_durations(self) -> Tuple[int, int]:
        return 50*60, 10*60

class Custom:
    def __init__(self, focus_sec: int, break_sec: int) -> None:
        # TODO M3: validare che i valori siano > 0 (ValueError altrimenti)
        self.focus_sec = focus_sec
        self.break_sec = break_sec

    def get_durations(self) -> Tuple[int, int]:
        return self.focus_sec, self.break_sec
