# Argomenti Extra per Ampliare il Percorso

Questo documento raccoglie temi non approfonditi nel corso principale ma utili per evolvere come sviluppatori Python. Ogni sezione include una breve descrizione e un esempio pratico per iniziare a sperimentare.

---

## 1. Programmazione Concorrente: `asyncio` e `await`

Python offre il modulo `asyncio` per gestire IO concorrente senza bloccare il thread principale. È ideale per chiamate HTTP parallele o task periodici leggeri.

```python
import asyncio
import random

async def fetch_sensor(sensor_id: int) -> float:
    await asyncio.sleep(random.uniform(0.1, 0.5))  # simuliamo IO
    return 20.0 + sensor_id * 0.5

async def main() -> None:
    readings = await asyncio.gather(*(fetch_sensor(i) for i in range(3)))
    print("Letture:", readings)

asyncio.run(main())
```

---

## 2. Data Validation e Serializzazione con `pydantic`

`pydantic` consente di validare dati in ingresso tramite modelli tipizzati. È ampiamente usato in FastAPI e in contesti di ingestione dati.

```python
from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    name: str
    email: EmailStr
    salary: float

payload = {"name": "Alice", "email": "alice@example.com", "salary": 42000}
employee = Employee(**payload)
print(employee.json())
```

---

## 3. Costruire API REST con FastAPI

FastAPI permette di creare endpoint HTTP tipizzati in modo rapido, con documentazione automatica Swagger/OpenAPI.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/saluta/{nome}")
def saluta(nome: str) -> dict[str, str]:
    return {"messaggio": f"Ciao {nome}!"}

# Avvia con: uvicorn app:app --reload
```

---

## 4. Gestione Asincrona di Task con Celery

Per eseguire job in background o pianificare task periodici è comune usare Celery con un broker (Redis/RabbitMQ). Di seguito un esempio minimale di task.

```python
from celery import Celery

app = Celery("notifiche", broker="redis://localhost:6379/0")

@app.task
def invia_report(email: str) -> str:
    return f"Report inviato a {email}"

# Da shell: celery -A module_name worker --loglevel=INFO
```

---

## 5. Tipi Avanzati con `typing` e `mypy`

Per progetti ampi è utile staticare i controlli tramite `mypy`. Tipi come `TypedDict`, `Literal` e `Protocol` aumentano l’espressività.

```python
from typing import TypedDict, Literal

class JobConfig(TypedDict):
    mode: Literal["test", "prod"]
    retries: int

def run_job(config: JobConfig) -> None:
    if config["mode"] == "prod":
        print("Esecuzione in produzione")
    else:
        print("Esecuzione in test")

run_job({"mode": "test", "retries": 3})
```

---

## 6. Packaging Professionale con `pyproject.toml`

Le moderne librerie Python usano `pyproject.toml` per definire metadata, dipendenze e strumenti di build come Poetry o Hatch.

```toml
[project]
name = "analytics-helper"
version = "0.1.0"
description = "Utility per analisi HR"
requires-python = ">=3.12"
dependencies = ["pandas>=2.1", "matplotlib>=3.8"]

[tool.poetry.scripts]
report = "analytics.cli:main"
```

---

## 7. Sicurezza: Gestione Segreti e Variabili d’Ambiente

È buona pratica separare i segreti dal codice. Il pacchetto `python-dotenv` consente di caricare variabili da file `.env`.

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["API_KEY"]
print("API Key caricata:", api_key[:4] + "****")
```

---

## 8. Scraping Web con `BeautifulSoup`

Per estrarre dati da pagine HTML possiamo combinare `requests` e `BeautifulSoup`.

```python
import requests
from bs4 import BeautifulSoup

def estrai_titoli(url: str) -> list[str]:
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    return [h2.get_text(strip=True) for h2 in soup.select("h2")]

print(estrai_titoli("https://realpython.com/"))
```

---

## 9. Grafici Interattivi con `plotly`

Per dashboard web-ready, `plotly` genera grafici interattivi condivisibili online.

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({"anno": [2021, 2022, 2023], "ricavo": [2.5, 3.1, 3.8]})
fig = px.bar(df, x="anno", y="ricavo", title="Ricavi annuali")
fig.write_html("ricavi.html")
```

---

## 10. Integrazione CI/CD con GitHub Actions

Automatizzare test e linting garantisce qualità costante. Un workflow YAML minimo:

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest
```

---

## 11. Microservices e Messaggistica con `FastAPI` + `Kafka`

Per architetture event-driven, un microservizio può pubblicare messaggi su Kafka. L'esempio mostra l'invio asincrono.

```python
from fastapi import FastAPI
from aiokafka import AIOKafkaProducer
import asyncio

app = FastAPI()
producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")

@app.on_event("startup")
async def startup_event():
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()

@app.post("/log")
async def log_event(message: str) -> dict[str, str]:
    await producer.send_and_wait("events", message.encode())
    return {"status": "queued"}
```

---

## 12. Benchmarking con `timeit` e `cProfile`

Misurare le prestazioni è fondamentale prima di ottimizzare. `timeit` valuta snippet, `cProfile` analizza call stack e tempi.

```python
import timeit

def crea_lista():
    return [i * 2 for i in range(10_000)]

print(timeit.timeit(crea_lista, number=100))
```

Per analisi più approfondite:

```python
import cProfile

cProfile.run("crea_lista()")
```

---

## 13. Parallelismo CPU-bound con `multiprocessing`

Per carichi CPU intensivi conviene usare processi separati (evitando il GIL). L'esempio calcola numeri primi in parallelo.

```python
from multiprocessing import Pool

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

with Pool() as pool:
    primes = pool.map(is_prime, range(10_000, 10_100))
```

---

## 14. Documentazione API con `Sphinx`

Sphinx genera documentazione HTML a partire da docstring strutturate.

```python
def calcola_bonus(salary: float) -> float:
    """Calcola il bonus annuale.

    :param salary: stipendio base annuale
    :returns: bonus pari al 10% dello stipendio
    """
    return salary * 0.10
```

Il comando `sphinx-quickstart` crea lo scaffold; le docstring sono poi convertite in HTML con `make html`.

---

## 15. Kubernetes per Deploy Scalabili

Una configurazione `Deployment` gestisce repliche e aggiornamenti rolling.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: analytics-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: analytics
  template:
    metadata:
      labels:
        app: analytics
    spec:
      containers:
        - name: web
          image: ghcr.io/utente/analytics:latest
          ports:
            - containerPort: 8000
```

---

Questi argomenti completano il quadro di competenze per un percorso Python moderno. Scegli un tema per volta, integra esercizi e progetti personali e condividi i progressi con la community. Buon apprendimento! 🚀
