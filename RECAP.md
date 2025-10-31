# Corso Python – Recap Esteso

Questo documento di recap riassume l'intero percorso del corso “PythonMM”. È pensato come materiale di ripasso in **dieci pagine equivalenti** divise in **cinque macro-argomenti**. Ogni sezione contiene paragrafi discorsivi, tabelle di riepilogo ed esempi di codice tratti o ispirati dai progetti della repository.

---

## 1. Fondamenti del Linguaggio e Strutture Dati

### 1.1 Sintassi di base

Python privilegia la leggibilità: blocchi indentati, tipizzazione dinamica e semantica orientata agli oggetti. Ricorda che ogni elemento è un oggetto e che le funzioni sono cittadini di prima classe.

```python
def saluta(nome: str, formal: bool = False) -> str:
    titolo = "Buongiorno" if formal else "Ciao"
    return f"{titolo}, {nome}!"

print(saluta("Marius"))
print(saluta("Marius", formal=True))
```

### 1.2 Contenitori built-in

Le strutture dati principali sono liste, tuple, set e dizionari. Le comprehension permettono di trasformare collezioni in modo conciso.

```python
numeri = [1, 2, 3, 4, 5]
quadrati = [n ** 2 for n in numeri if n % 2 == 1]

impostazioni = {"debug": True, "workers": 4}
valori_di_default = {**impostazioni, "workers": impostazioni.get("workers", 1)}
```

| Struttura | Mutabile | Ordinata | Use case principale |
| --- | --- | --- | --- |
| Lista | Sì | Sì | Sequenze dinamiche, stack, queue |
| Tupla | No | Sì | Record immutabili, chiavi di dict |
| Set | Sì | No | Deduplica elementi, operazioni insiemistiche |
| Dict | Sì | Sì (3.7+) | Mappare chiavi a valori |

### 1.3 Funzioni, args e kwargs

La possibilità di usare parametri posizionali e nominali rende le API flessibili. Il pattern `*args` e `**kwargs` consente di gestire casi variabili.

```python
def report(titolo: str, *righe: str, **metadata: str) -> str:
    corpo = "\n".join(righe)
    footer = " | ".join(f"{k}={v}" for k, v in metadata.items())
    return f"== {titolo} ==\n{corpo}\n-- {footer}"

print(report("Log giornaliero", "Step 1 completato", "Step 2 completato", autore="Analyst"))
```

### 1.4 Error handling e typing

Gestire le eccezioni è fondamentale per un codice robusto. Le annotazioni di tipo (PEP 484) aiutano i tool statici senza influire sull'esecuzione runtime.

```python
from typing import Iterable

def media(valori: Iterable[float]) -> float:
    valori = list(valori)
    if not valori:
        raise ValueError("La lista non può essere vuota")
    return sum(valori) / len(valori)

try:
    media([])
except ValueError as exc:
    print(f"Errore calcolando la media: {exc}")
```

---

## 2. Funzioni Avanzate e Programmazione Funzionale

### 2.1 Lambda, map, filter, reduce

Le espressioni lambda permettono funzioni inline. `map`, `filter` e `functools.reduce` consentono pipeline di trasformazioni.

```python
from functools import reduce

numeri = range(1, 6)
somma = reduce(lambda acc, n: acc + n, numeri)
pari = list(filter(lambda n: n % 2 == 0, numeri))
```

### 2.2 Generatori e lazy evaluation

Generatori e generator expression riducono l'uso di memoria e permettono stream infiniti.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

primi_cinque = [next(fibonacci()) for _ in range(5)]
print(primi_cinque)
```

### 2.3 Decorator

I decorator avvolgono funzioni o classi aggiungendo funzionalità. Il corso fornisce esempi quando introduce logging e caching.

```python
from functools import wraps
from time import perf_counter

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{func.__name__} ha impiegato {elapsed:.3f}s")
        return result
    return wrapper

@measure
def elabora(n: int) -> int:
    return sum(i * i for i in range(n))
```

### 2.4 Protocol e duck typing

Con Python 3.8+ possiamo descrivere il comportamento atteso tramite `typing.Protocol`, come visto negli esercizi TDD.

```python
from typing import Protocol

class Notificatore(Protocol):
    def manda_alert(self, messaggio: str) -> None:
        ...

def avvisa(notif: Notificatore, testo: str) -> None:
    notif.manda_alert(testo)
```

---

## 3. Programmazione a Oggetti e Design Pattern

### 3.1 Classi, ereditarietà e composizione

Il corso enfatizza l'uso di composizione e principi SOLID. Classi dataclass rendono più semplice definire modelli immutabili.

```python
from dataclasses import dataclass

@dataclass
class LetturaSensore:
    temperatura: float
    umidita: float
    timestamp: str
```

### 3.2 Pattern creazionali (Singleton, Factory, Builder, Prototype, Abstract Factory)

La cartella `design-patterns-todo2-python/creational` contiene scheletri, test e soluzioni. L'esempio seguente mostra un Singleton configurato:

```python
class AppConfig:
    _instance = None
    _initialized = False

    def __new__(cls, app_name: str, debug: bool = False):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, app_name: str, debug: bool = False):
        if self.__class__._initialized:
            return
        self.app_name = app_name
        self.debug = debug
        self.__class__._initialized = True
```

### 3.3 Pattern strutturali (Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy)

Questi pattern gestiscono la composizione di classi. Il Decorator aggiunge responsabilità senza alterare l'oggetto originale.

```python
class DataSource:
    def read(self) -> str:
        raise NotImplementedError

    def write(self, data: str) -> None:
        raise NotImplementedError

class SimpleDataSource(DataSource):
    def __init__(self) -> None:
        self._buffer = ""

    def read(self) -> str:
        return self._buffer

    def write(self, data: str) -> None:
        self._buffer = data

class LoggingDataSource(DataSource):
    def __init__(self, wrapped: DataSource) -> None:
        self._wrapped = wrapped

    def read(self) -> str:
        print("[LOG] read")
        return self._wrapped.read()

    def write(self, data: str) -> None:
        print(f"[LOG] write {data}")
        self._wrapped.write(data)
```

### 3.4 Pattern comportamentali (Strategy, State, Command, Observer, Iterator, Chain of Responsibility, Mediator, Memento, Template Method, Visitor, Interpreter)

```python
class TextFormatStrategy:
    def format(self, text: str) -> str:
        raise NotImplementedError

class UpperCaseStrategy(TextFormatStrategy):
    def format(self, text: str) -> str:
        return text.upper()

class TextFormatter:
    def __init__(self, strategy: TextFormatStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: TextFormatStrategy) -> None:
        self._strategy = strategy

    def format(self, text: str) -> str:
        return self._strategy.format(text)
```

### 3.5 Principi SOLID e refactoring

Nel modulo SensoriMonitor.TDD il percorso guida il refactor orientato a SRP, inversione delle dipendenze e riduzione delle duplicazioni. Ogni milestone suggerisce refactoring graduali protetti dai test.

---

## 4. Automazione, Test-Driven Development e Tooling

### 4.1 Pytest e struttura dei test

Gli esercizi più complessi includono file `tests/` con casi preimpostati. Pytest consente fixture modulari, parametrizzazione e report dettagliati.

```python
import pytest
from monitor import MonitorAmbientale, LetturaSensore

@pytest.fixture
def monitor():
    return MonitorAmbientale()

def test_aggiungi_lettura(monitor):
    monitor.aggiungi_lettura(LetturaSensore(temperatura=22.0, umidita=40.0, timestamp="2024-01-01"))
    assert len(monitor.tutte_le_letture()) == 1
```

### 4.2 Ciclo TDD (Red → Green → Refactor)

Il progetto `SensoriMonitor.TDD` è organizzato in milestone che impongono la sequenza TDD:

1. Scrivi un test con `TODO`.
2. Osserva il fallimento (Red).
3. Implementa la soluzione minima (Green).
4. Refactor mantenendo i test verdi.

### 4.3 Mocks e inversione delle dipendenze

L'uso del modulo `unittest.mock` (o fixture pytest) consente di isolare componenti. Nell'esercizio TDD, il notificatore esterno viene mockato per verificare l'invio di alert.

```python
from unittest.mock import Mock

notificatore = Mock()
monitor = MonitorAmbientale(notificatore=notificatore)
monitor.verifica_allarme()
notificatore.manda_alert.assert_called_once()
```

### 4.4 Gestione ambienti e requirements

Ogni progetto suggerisce l'uso di ambienti virtuali (`python -m venv`) e file `requirements.txt`. Alcuni moduli usano `pytest`, altri librerie per la data analysis.

### 4.5 Automazione e CLI

Il corso include esercizi che costruiscono CLI o processi schedulati (es. piattaforma notifiche). Si enfatizza l'uso di `argparse`, logging e script idempotenti.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()

if args.debug:
    print("Modalità debug attiva")
```

---

## 5. Data Analysis, Reportistica e API

### 5.1 Pandas e analisi HR

La cartella `esercizi/06-hr-analytics/` fornisce dataset CSV, notebook e script orientati all'analisi HR. Si lavora su pulizia dati, groupby e reportistica.

```python
import pandas as pd

df = pd.read_csv("employees.csv")
per_team = df.groupby("department")["salary"].mean().sort_values(ascending=False)
print(per_team.head())
```

### 5.2 Notebook interattivi

I notebook (`notebook/HR_Analysis_OOP_walkthrough.ipynb`) accompagnano gli esercizi con walkthrough guidati. Vengono utilizzati per generare grafici e dashboard rapide.

### 5.3 API e integrazione esterna

`esercizi/07-randomuser/` mostra come consumare API esterne, validare i dati e trasformarli in report. L'esempio seguente usa `requests` e dataclass.

```python
import requests
from dataclasses import dataclass

@dataclass
class Utente:
    nome: str
    email: str
    paese: str

def scarica_utenti(n: int = 5) -> list[Utente]:
    risposta = requests.get(f"https://randomuser.me/api/?results={n}", timeout=10)
    risposta.raise_for_status()
    payload = risposta.json()["results"]
    return [
        Utente(nome=f"{item['name']['first']} {item['name']['last']}",
               email=item["email"],
               paese=item["location"]["country"])
        for item in payload
    ]
```

### 5.4 Reportistica automatizzata

Il progetto HR utilizza template e funzioni di export (CSV, PDF). In particolare, `hr_analysis.py` costruisce pipeline di analisi replicabili.

### 5.5 Visualizzazione dati

Le slide 09-11 introducono `matplotlib` e `seaborn`. Un esempio minimo:

```python
import matplotlib.pyplot as plt

anni = [2020, 2021, 2022, 2023]
ricavi = [2.5, 3.0, 3.8, 4.5]

plt.plot(anni, ricavi, marker="o")
plt.title("Ricavi annuali (MLN €)")
plt.xlabel("Anno")
plt.ylabel("Ricavi")
plt.grid(True)
plt.show()
```

---

## Conclusioni e Prossimi Passi

Questo recap propone una vista d'insieme dei contenuti affrontati nel corso:

- **Fondamenti del linguaggio**: sintassi, funzioni, gestione errori, type hints.
- **Programmazione avanzata**: generatori, decorator, protocolli e funzionale.
- **OOP e design pattern**: creazionali, strutturali, comportamentali, SOLID.
- **Testing e TDD**: pytest, mocks, environmental setup, cicli TDD.
- **Data analysis e integrazione**: Pandas, API, reportistica e visualizzazioni.

Per consolidare:

1. Ripeti gli esercizi a distanza di tempo senza consultare le soluzioni.
2. Integra i pattern GoF in mini-progetti personali.
3. Automatizza i test nel tuo ambiente CI/CD (GitHub Actions, GitLab CI).
4. Approfondisci l'analisi dati con dataset reali e notebook interattivi.
5. Sperimenta librerie aggiuntive come FastAPI, SQLModel, Pydantic per costruire servizi più complessi.

Buon proseguimento nel tuo percorso Python! 🐍✨
