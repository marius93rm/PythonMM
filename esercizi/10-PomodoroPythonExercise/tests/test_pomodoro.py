import pytest
from dataclasses import dataclass
from pomodoro.core import Pomodoro
from pomodoro.sessions import Custom
from pomodoro.notify import INotifier
from pomodoro.timer import TimerService

class FakeTick:
    def tick(self): pass

class FakeTimer(TimerService):
    def __init__(self):
        super().__init__(FakeTick())
        self.calls = []

    def countdown(self, seconds, *, on_tick, on_completed):
        # Simula chiamando on_tick ogni secondo immediatamente
        for s in range(seconds, 0, -1):
            on_tick(s)
        on_completed()
        self.calls.append(seconds)

class SpyNotifier(INotifier):
    def __init__(self):
        self.messages = []
    def notify(self, message: str) -> None:
        self.messages.append(message)

@dataclass
class InMemoryRepo:
    logs: list
    def save(self, log) -> None:
        self.logs.append(log)

def test_pomodoro_notifies_and_logs_and_event():
    strategy = Custom(3, 2)  # piccole durate per test
    notifier = SpyNotifier()
    timer = FakeTimer()
    repo = InMemoryRepo([])

    p = Pomodoro(strategy, notifier=notifier, timer=timer, repo=repo)

    event_called = {"x": False}
    p.on_focus_completed = lambda: event_called.__setitem__("x", True)

    with pytest.raises(NotImplementedError):
        # finché M4/M5 non è implementata
        p.run()

    # Quando implementi M4/M5, rimuovi la riga sopra e verifica:
    # p.run()
    # assert "Focus finito!" in notifier.messages[-2]
    # assert "Break finito!" in notifier.messages[-1]
    # assert event_called["x"] is True
    # assert len(repo.logs) == 2
    # kinds = [log.kind for log in repo.logs]
    # assert kinds == ["focus", "break"]
    # assert timer.calls == [3, 2]
