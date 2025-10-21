# 🕒 Pomodoro Focus Timer — Esercizio Python con SOLID + Test

Benvenuto! In questo esercizio costruirai un **Pomodoro Focus Timer** in **Python** applicando i principi **SOLID** in modo concreto.
Il progetto include **test automatici (pytest)** e file con porzioni **TODO** da completare.

---

## 🎯 Obiettivi didattici

- Applicare **SRP, OCP, DIP, ISP** su un caso reale in Python.
- Usare **astrazioni leggere** (Protocol/ABC) per separare **timer**, **notifiche**, **strategie**, **persistenza**.
- Scrivere codice **testabile** con dipendenze iniettabili.
- Eseguire **pytest** per validare il comportamento.

---

## 📦 Struttura progetto

```
PomodoroPythonExercise/
├─ pyproject.toml
├─ src/
│  └─ pomodoro/
│     ├─ __init__.py
│     ├─ timer.py               <-- TODO principali
│     ├─ notify.py
│     ├─ sessions.py
│     ├─ persistence.py         <-- TODO
│     ├─ core.py                <-- TODO
│     └─ runner.py
└─ tests/
   ├─ test_timer.py
   ├─ test_pomodoro.py
   ├─ test_strategies.py
   └─ test_repository.py
```

---

## 🔎 Breve teoria (con esempio)

- **SRP**: una classe = una responsabilità (es. `TimerService` conta il tempo, **non** invia notifiche).
- **DIP**: dipendi da **interfacce** (Protocol/ABC), non da classi concrete (`Pomodoro` dipende da `INotifier`, non da `print`).
- **OCP**: estendi con nuove strategie senza toccare il codice esistente (`ISessionStrategy` → `Classic25_5`, `Deep50_10`, `Custom`).
- **ISP**: interfacce **piccole e mirate** (es. `INotifier` con un solo metodo).

**Esempio minimo di DIP + OCP (Python):**
```python
from typing import Protocol, Tuple

class INotifier(Protocol):
    def notify(self, message: str) -> None: ...

class ConsoleNotifier:
    def notify(self, message: str) -> None:
        print(message)

class ISessionStrategy(Protocol):
    def get_durations(self) -> Tuple[int, int]: ...

class Classic25_5:
    def get_durations(self) -> Tuple[int, int]:
        return 25*60, 5*60
```

---

## 🧱 Milestones

1. **Timer minimo (SRP)** — Implementa `TimerService.countdown` usando `ITickProvider` per scandire i secondi.
2. **Notifiche (DIP + ISP)** — Usa `INotifier` per inviare messaggi di fine sessione.
3. **Strategie (OCP)** — Implementa `ISessionStrategy` per durate `25/5` e `50/10` (+ custom).
4. **Evento completamento (Observer-like)** — In `Pomodoro`, pubblica un callback/evento quando il focus finisce.
5. **Persistenza (SRP + DIP)** — `CsvSessionRepository` salva il log delle sessioni in `sessions.csv`.
6. **Runner** — In `runner.py`, esegui focus e break in sequenza mostrando il countdown.
7. **(Extra “wow”) Progress bar** — opzionale: una barra di avanzamento in console.

---

## ▶️ Come eseguire

Consigliato Python **3.10+** (ok anche 3.11/3.12).

```bash
# attiva (opzionale) un venv e installa pytest se non l'hai già
# python -m venv .venv && source .venv/bin/activate  # mac/linux
# .venv\Scripts\activate                              # windows
pip install -U pytest

# esegui i test (inizialmente falliranno finché non completi i TODO)
pytest

# avvia il runner (usa durate molto brevi in demo con Custom)
python -m pomodoro.runner
```

---

## ✅ Cosa verificano i test

- Che `TimerService` chiami `on_tick` correttamente e `on_completed` alla fine.
- Che `Pomodoro` notifichi al termine del focus e chiami un `on_completed` registrato.
- Che le **strategie** restituiscano le durate attese e che `Custom` validi gli input.
- Che il **repository CSV** salvi una riga ben formata.

> Nota: i test sono progettati perché inizialmente **falliscano** finché non completi i TODO.

---

## 📊 Criteri di valutazione (0–3)

- **0** = non esegue, test falliscono in massa, struttura non rispettata.
- **1** = parziale: timer o strategie ok, ma mancano notifiche/persistenza o design non SOLID.
- **2** = funziona: tutti i test verdi, codice chiaro, SOLID applicato.
- **3** = completo/pro: extra “wow” (progress bar, CLI pulita), tipizzazione e docstring curate.
