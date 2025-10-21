from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Optional
from datetime import datetime

from .timer import TimerService, ITickProvider
from .notify import INotifier, ConsoleNotifier
from .sessions import ISessionStrategy
from .persistence import ISessionRepository, CsvSessionRepository, SessionLog

@dataclass
class Pomodoro:
    strategy: ISessionStrategy
    notifier: INotifier = field(default_factory=ConsoleNotifier)
    timer: TimerService = field(default_factory=TimerService)
    repo: ISessionRepository = field(default_factory=CsvSessionRepository)

    # callback chiamata al termine del focus (Observer-like)
    on_focus_completed: Optional[Callable[[], None]] = None

    def run(self) -> None:
        """
        Esegue un ciclo focus -> break secondo la strategia.
        TODO M4 + M5:
        - Ricava (focus_sec, break_sec) dalla strategia.
        - Avvia un countdown per il focus che:
            * alla fine notifichi "Focus finito!"
            * pubblichi l'evento on_focus_completed se presente
            * salvi un SessionLog(kind='focus', seconds=focus_sec)
        - Avvia un countdown per il break che alla fine notifichi "Break finito!" e salvi il log.
        Nota: i test useranno un FakeTickProvider per non attendere davvero.
        """
        focus_sec, break_sec = self.strategy.get_durations()

        # TODO: implementare come descritto sopra usando self.timer.countdown(...)
        raise NotImplementedError("Implementa Pomodoro.run (Milestone 4 & 5)")
