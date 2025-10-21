from __future__ import annotations
from typing import Protocol

class INotifier(Protocol):
    def notify(self, message: str) -> None: ...

class ConsoleNotifier:
    def notify(self, message: str) -> None:
        print(message)

class BeepNotifier:
    """Semplice 'beep' testuale per ambienti senza suono reale."""
    def notify(self, message: str) -> None:
        print("\a" + message)  # \a = bell; spesso silenziato, ma va bene per demo
