import pytest
from pomodoro.timer import TimerService

class FakeTick:
    def __init__(self):
        self.count = 0
    def tick(self):
        self.count += 1

def test_timer_calls_on_tick_and_on_completed():
    fake = FakeTick()
    t = TimerService(fake)
    ticks = []
    completed = {"done": False}

    def on_tick(left: int):
        ticks.append(left)

    def on_completed():
        completed["done"] = True

    with pytest.raises(NotImplementedError):
        # finché M1 non è implementata, è ok che sollevi
        t.countdown(3, on_tick=on_tick, on_completed=on_completed)

    # Quando implementi M1, rimuovi la riga sopra e verifica:
    # t.countdown(3, on_tick=on_tick, on_completed=on_completed)
    # assert ticks == [3,2,1]
    # assert completed["done"] is True
    # assert fake.count == 3
