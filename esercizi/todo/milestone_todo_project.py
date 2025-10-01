# milestone_todo_project.py
# Progetto a step: "Mini To‑Do Manager" con milestones progressive.
#
# OBIETTIVO
# Costruire, per passi successivi (milestones), un piccolo gestore di task
# con persistenza su file, import/export, filtri e formattazione.
#
# COME LAVORARE
# - Leggi i docstring di ogni funzione e implementa al posto di "pass".
# - Esegui questo file: vedrai il report dei test milestones superati.
# - Ogni milestone sblocca nuove feature. Non saltare i passi.
#
# NON usare librerie esterne. Puoi usare SOLO la standard library.
# Suggerite: json, csv, datetime, os, tempfile, itertools, typing.
# Python >= 3.10 consigliato.

from __future__ import annotations

import csv
import json
import os
import tempfile
from dataclasses import dataclass
from datetime import date
from typing import Iterable, Optional

# =============================================================
# DATA MODEL
# =============================================================

@dataclass
class Task:
    """Rappresentazione di un task.
    Campi previsti:
      - id: int (assegnato automaticamente, progressivo, >=1)
      - title: str (titolo conciso)
      - priority: int (1..5, default=3)
      - due: Optional[str] (formato 'YYYY-MM-DD' oppure None)
      - done: bool (default=False)
      - tags: list[str] (tutte minuscole, uniche, ordinate)
      - created: str (data odierna 'YYYY-MM-DD')
    """
    id: int
    title: str
    priority: int = 3
    due: Optional[str] = None
    done: bool = False
    tags: list[str] = None
    created: str = None


# =============================================================
# M1) add_task + list_tasks (base)
# =============================================================
def add_task(tasks: list[Task],
             title: str,
             priority: int = 3,
             due: Optional[str] = None,
             tags: Optional[Iterable[str]] = None) -> Task:
    """Milestone 1: Aggiungi un task di base a 'tasks' e restituiscilo.

    Requisiti M1 (MINIMO)
    - id progressivo: 1 per il primo task, poi 2, 3, ...
    - title usato "as-is" (normalizzazione arriva più avanti)
    - priority usata "as-is"
    - due usata "as-is"
    - done False di default
    - tags convertite in lista se non None (ma senza normalizzazione per ora)
    - created = data odierna (YYYY-MM-DD)

    Suggerimento: prendi l'ultimo id in 'tasks' e somma 1,
                  altrimenti usa 1 se lista vuota.
    """
    pass


def list_tasks(tasks: list[Task]) -> list[Task]:
    """Milestone 1: Ritorna una *shallow copy* della lista dei task.

    Requisiti M1 (MINIMO)
    - Non ordinare, non filtrare: semplicemente copia in una nuova lista.
    - Non mutare l'input.
    """
    pass


# =============================================================
# M2) save_db + load_db (persistenza JSON)
# =============================================================
def save_db(path: str, tasks: list[Task]) -> None:
    """Milestone 2: Salva 'tasks' in formato JSON sul percorso 'path'.

    Requisiti M2
    - Formato: lista di dict (serializza i dataclass Task).
    - Usa UTF-8, indentazione 2, ensure_ascii=False.
    - Il path deve essere sovrascritto se già esiste.
    """
    pass


def load_db(path: str) -> list[Task]:
    """Milestone 2: Carica un elenco di Task da un file JSON 'path'.

    Requisiti M2
    - Se il file non esiste, ritorna lista vuota.
    - Deserializza ciascun dict in un Task.
    - Non validare qui: è compito di M5.
    """
    pass


# =============================================================
# M3) toggle_done + remove_task
# =============================================================
def toggle_done(tasks: list[Task], task_id: int, done: bool = True) -> bool:
    """Milestone 3: Imposta lo stato 'done' del task con id=task_id.

    Ritorna True se trovato e aggiornato, altrimenti False.
    """
    pass


def remove_task(tasks: list[Task], task_id: int) -> bool:
    """Milestone 3: Rimuovi il task con id=task_id da 'tasks'.

    Ritorna True se rimosso, False se non trovato.
    """
    pass


# =============================================================
# M4) Filtri + Ordinamenti
# =============================================================
def list_tasks_adv(tasks: list[Task],
                   only_open: Optional[bool] = None,
                   tag: Optional[str] = None,
                   order_by: str = 'id') -> list[Task]:
    """Milestone 4: Lista avanzata con filtri e ordinamento.

    - Filtri:
        only_open = True  -> mostra solo non conclusi
        only_open = False -> mostra solo conclusi
        only_open = None  -> nessun filtro per stato
        tag = 'foo'       -> mostra solo i task che contengono questo tag (case-insensitive)

    - Ordinamenti (order_by): 'id' (default), 'priority', 'due', 'title'
      Nota: per 'due' con valori None, mettili *dopo* quelli con data.
    """
    pass


# =============================================================
# M5) Normalizzazione input + validazione
# =============================================================
def parse_due(s: Optional[str]) -> Optional[str]:
    """Milestone 5: Parsing della data di scadenza.

    - Accetta None o stringhe 'YYYY-MM-DD'. Se il formato è valido, ritorna la stringa.
      Se non valido o vuota, ritorna None.
    """
    pass


def normalize_task_fields(title: str,
                          priority: int = 3,
                          tags: Optional[Iterable[str]] = None,
                          due: Optional[str] = None) -> tuple[str, int, list[str], Optional[str]]:
    """Milestone 5: Normalizza titolo, priorità, tags, due.

    Regole:
    - title: strip, collassa spazi multipli ad uno; se vuoto -> ValueError
    - priority: clamp in [1,5]
    - tags: se None -> []; altrimenti: lowercase, trim, rimuovi vuoti, unici, ordinati
    - due: usa parse_due
    """
    pass


# =============================================================
# M6) Statistiche
# =============================================================
def stats(tasks: list[Task]) -> dict:
    """Milestone 6: Ritorna un dizionario con statistiche:
    {
      'total': int,
      'open': int,
      'done': int,
      'by_tag': {tag: count_totale}
    }
    """
    pass


# =============================================================
# M7) Export CSV
# =============================================================
def export_csv(tasks: list[Task], path: str) -> None:
    """Milestone 7: Esporta i task in CSV con header:
    id,title,priority,due,done,tags,created
    - 'tags' uniti da '|' (pipe) nell'ordine già presente.
    - UTF-8, newline=''
    """
    pass


# =============================================================
# M8) Import CSV (merge con dedupe)
# =============================================================
def import_csv(tasks: list[Task], path: str) -> int:
    """Milestone 8: Importa task da CSV e uniscili a 'tasks'.

    - Dedupe: non importare righe che duplicano (title case-insensitive, due uguale)
    - Assegna nuovi id progressivi coerenti con 'tasks' esistenti.
    - Ritorna il numero di task effettivamente importati.
    - Normalizza con le regole di M5.
    """
    pass


# =============================================================
# M9) Formattazione leggibile
# =============================================================
def format_task(t: Task) -> str:
    """Milestone 9: Ritorna una stringa compatta e leggibile del task.

    Esempi:
    - "[ ] #3 (P2) Compra latte — due 2025-12-01 — tags: casa,spesa"
    - "[x] #1 (P5) Progetto — tags: lavoro"
    (Ometti parti vuote: se niente due o tags, non stamparle)
    """
    pass


# =============================================================
# M10) (facoltativa) CLI testabile "non interattiva"
# =============================================================
def demo_scenario_non_interattivo(tmpdir: Optional[str] = None) -> dict:
    """Milestone 10 (facoltativa):
    Esegui un mini-scenario end-to-end senza input dell'utente, così è testabile.

    Passi suggeriti:
      - crea 3 task
      - salva su JSON
      - ricarica
      - esporta CSV
      - re-importa (nessun duplicato atteso)
      - calcola stats

    Ritorna un piccolo riepilogo con 'counts' e 'paths' usati.
    """
    pass


# =============================================================
# ================    TEST AUTOMATICI    ======================
# =============================================================

def _mk_tmpfile(suffix: str) -> str:
    fd, path = tempfile.mkstemp(suffix=suffix, text=True)
    os.close(fd)
    return path

def _today() -> str:
    return date.today().isoformat()

def run_milestone_tests():
    ok = []

    # ----------------- M1
    try:
        tasks: list[Task] = []
        t1 = add_task(tasks, 'Compra latte')
        assert isinstance(t1, Task)
        assert t1.id == 1 and t1.title == 'Compra latte' and t1.done is False
        assert t1.priority == 3 and t1.due is None and isinstance(t1.tags, list)
        assert t1.created == _today()
        t2 = add_task(tasks, 'Porta fuori il cane', priority=2)
        assert t2.id == 2
        lst = list_tasks(tasks)
        assert lst is not tasks and len(lst) == 2
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M2
    try:
        json_path = _mk_tmpfile('.json')
        save_db(json_path, tasks)
        tasks2 = load_db(json_path)
        assert len(tasks2) == 2 and tasks2[0].title == 'Compra latte'
        os.remove(json_path)
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M3
    try:
        assert toggle_done(tasks, 1, True) is True
        assert any(t.id == 1 and t.done for t in tasks)
        assert remove_task(tasks, 999) is False
        assert remove_task(tasks, 2) is True
        assert all(t.id != 2 for t in tasks)
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M4
    try:
        # crea un po' di dati
        add_task(tasks, 'Studia Python', priority=5, due='2025-12-01', tags=['Studio','Python'])
        add_task(tasks, 'Paga bollette', priority=2, due='2025-10-10', tags=['casa'])
        add_task(tasks, 'Compra uova', priority=4, tags=['Spesa'])

        opened = list_tasks_adv(tasks, only_open=True)
        assert all(not t.done for t in opened)

        python_only = list_tasks_adv(tasks, tag='python')
        assert all('python' in (t.tags or []) for t in python_only)

        by_due = list_tasks_adv(tasks, order_by='due')
        dues = [t.due for t in by_due if t.due is not None]
        assert dues == sorted(dues)  # None alla fine
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M5
    try:
        title, pr, tags, due = normalize_task_fields('  compra   Pane  ', priority=9,
                                                     tags=['Spesa','  ', 'Pane', 'spesa'],
                                                     due='2025-02-30')  # data invalida
        assert title == 'compra Pane'
        assert pr == 5
        assert tags == ['pane', 'spesa']
        assert due is None
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M6
    try:
        s = stats(tasks)
        assert set(s.keys()) == {'total','open','done','by_tag'}
        assert s['total'] == len(tasks)
        assert s['open'] + s['done'] == s['total']
        assert isinstance(s['by_tag'], dict)
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M7
    try:
        csv_path = _mk_tmpfile('.csv')
        export_csv(tasks, csv_path)
        assert os.path.getsize(csv_path) > 0
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M8
    try:
        tasks_before = len(tasks)
        imported = import_csv(tasks, csv_path)
        # potremmo avere 0 import perché sono duplicati
        assert imported >= 0
        assert len(tasks) >= tasks_before
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M9
    try:
        sample = tasks[0]
        s = format_task(sample)
        assert f'#{sample.id}' in s and ('[x]' in s or '[ ]' in s)
        ok.append(True)
    except Exception:
        ok.append(False)

    # ----------------- M10
    try:
        out = demo_scenario_non_interattivo()
        assert isinstance(out, dict)
        ok.append(True)
    except Exception:
        ok.append(False)

    passed = sum(ok)
    total = len(ok)
    print(f"\n✅ Milestones superate: {passed}/{total}")
    if passed < total:
        for i, flag in enumerate(ok, start=1):
            if not flag:
                print(f"- M{i} FALLITA")
    else:
        print("Tutte le milestones superano i test. Ottimo lavoro!\n")

if __name__ == '__main__':
    run_milestone_tests()
