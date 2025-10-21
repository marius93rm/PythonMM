from __future__ import annotations
from typing import Tuple
from .sessions import Custom, Classic25_5, Deep50_10, ISessionStrategy
from .core import Pomodoro

def choose_strategy() -> ISessionStrategy:
    print("Scegli strategia: [1] Classic 25/5  [2] Deep 50/10  [3] Custom breve demo (10s/5s)")
    choice = input("Scelta (1/2/3): ").strip()
    if choice == "1":
        return Classic25_5()
    if choice == "2":
        return Deep50_10()
    # default: piccole durate per demo
    return Custom(10, 5)

def main() -> None:
    strat = choose_strategy()
    pomodoro = Pomodoro(strat)
    print("Avvio Pomodoro...")
    try:
        pomodoro.run()
    except NotImplementedError:
        print("Completa i TODO prima di eseguire il runner.")
    print("Fine.")

if __name__ == "__main__":
    main()
