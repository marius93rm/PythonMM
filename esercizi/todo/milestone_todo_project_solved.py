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
from dataclasses import dataclass, asdict  # aggiungo asdict per serializzare Task
from datetime import date, datetime        # aggiungo datetime per validare date
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
    # Calcola il prossimo id: 1 se la lista è vuota, altrimenti max id + 1
    next_id = (max((t.id for t in tasks), default=0) + 1)  # genera il nuovo id progressivo
    # Converte i tag in lista; se None usa lista vuota (evita None in seguito)
    tag_list = list(tags) if tags is not None else []      # M1 non richiede normalizzazione
    # Data di creazione in formato YYYY-MM-DD
    created = date.today().isoformat()                     # salva la data odierna come stringa
    # Crea l'istanza Task con i valori passati "as-is"
    t = Task(id=next_id, title=title, priority=priority, due=due,
             done=False, tags=tag_list, created=created)   # istanzia il dataclass
    # Aggiunge il task alla lista mutabile fornita
    tasks.append(t)                                        # muta la lista in-place
    # Restituisce il task creato
    return t                                               # consente chaining o verifica nei test


def list_tasks(tasks: list[Task]) -> list[Task]:
    """Milestone 1: Ritorna una *shallow copy* della lista dei task.

    Requisiti M1 (MINIMO)
    - Non ordinare, non filtrare: semplicemente copia in una nuova lista.
    - Non mutare l'input.
    """
    # Ritorna una copia superficiale per evitare effetti collaterali su 'tasks'
    return tasks.copy()  # la shallow copy mantiene i riferimenti ai Task ma non la lista originale


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
    # Converte ciascun Task in dict serializzabile (usa asdict per sicurezza)
    data = [asdict(t) for t in tasks]                      # lista di dizionari serializzabili
    # Scrive il JSON su file con encoding UTF-8 e indentazione 2
    with open(path, 'w', encoding='utf-8') as f:           # apre/sovrascrive il file destinazione
        json.dump(data, f, ensure_ascii=False, indent=2)   # salva mantenendo i caratteri unicode


def load_db(path: str) -> list[Task]:
    """Milestone 2: Carica un elenco di Task da un file JSON 'path'.

    Requisiti M2
    - Se il file non esiste, ritorna lista vuota.
    - Deserializza ciascun dict in un Task.
    - Non validare qui: è compito di M5.
    """
    # Se il file non esiste, ritorna lista vuota come richiesto
    if not os.path.exists(path):                           # controlla l'esistenza del file
        return []                                          # nessun dato da caricare
    # Legge il contenuto JSON dal file
    with open(path, 'r', encoding='utf-8') as f:           # apre il file in lettura
        data = json.load(f)                                # carica la lista di dizionari
    # Converte ogni dict in un'istanza Task senza validazione
    return [Task(**item) for item in data]                 # unpack dei campi nel costruttore


# =============================================================
# M3) toggle_done + remove_task
# =============================================================
def toggle_done(tasks: list[Task], task_id: int, done: bool = True) -> bool:
    """Milestone 3: Imposta lo stato 'done' del task con id=task_id.

    Ritorna True se trovato e aggiornato, altrimenti False.
    """
    # Itera sui task alla ricerca dell'id corrispondente
    for t in tasks:                                        # scorre la lista mutabile
        if t.id == task_id:                                # confronta l'id
            t.done = done                                  # aggiorna lo stato richiesto
            return True                                    # conferma l'aggiornamento
    # Se non trovato, ritorna False
    return False                                           # nessun task con quell'id


def remove_task(tasks: list[Task], task_id: int) -> bool:
    """Milestone 3: Rimuovi il task con id=task_id da 'tasks'.

    Ritorna True se rimosso, False se non trovato.
    """
    # Cerca l'indice del task con l'id specificato
    for i, t in enumerate(tasks):                          # enumerazione utile per indice
        if t.id == task_id:                                # verifica l'id
            del tasks[i]                                   # elimina l'elemento in posizione i
            return True                                    # rimozione avvenuta
    # Se non trovato, ritorna False
    return False                                           # nessuna rimozione effettuata


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
    # Inizia da una copia per non mutare la lista originale
    res = tasks.copy()                                     # copia superficiale
    # Applica filtro stato aperto/chiuso se richiesto
    if only_open is True:                                  # caso: mostra solo open
        res = [t for t in res if not t.done]               # filtra i non conclusi
    elif only_open is False:                               # caso: mostra solo done
        res = [t for t in res if t.done]                   # filtra i conclusi
    # Applica filtro tag if fornito (case-insensitive)
    if tag is not None:                                    # se un tag è richiesto
        tag_l = tag.lower()                                # portiamo in minuscolo il filtro
        res = [t for t in res if tag_l in (t.tags or [])]  # include solo task che contengono il tag
    # Scegli la chiave di ordinamento in base a order_by
    if order_by == 'id':                                   # ordinamento per id crescente
        keyfunc = lambda t: t.id
    elif order_by == 'priority':                           # ordinamento per priorità crescente
        keyfunc = lambda t: t.priority
    elif order_by == 'title':                              # ordinamento alfabetico per titolo
        keyfunc = lambda t: (t.title or '').lower()
    elif order_by == 'due':                                # ordinamento per scadenza
        # Prima quelli con data, poi i None (mettendo True/False come primo elemento)
        keyfunc = lambda t: (t.due is None, t.due or '')
    else:                                                  # fallback sicuro in caso di valore inatteso
        keyfunc = lambda t: t.id
    # Ritorna la lista ordinata secondo la chiave scelta
    return sorted(res, key=keyfunc)                        # non muta 'res', restituisce ordinata


# =============================================================
# M5) Normalizzazione input + validazione
# =============================================================
def parse_due(s: Optional[str]) -> Optional[str]:
    """Milestone 5: Parsing della data di scadenza.

    - Accetta None o stringhe 'YYYY-MM-DD'. Se il formato è valido, ritorna la stringa.
      Se non valido o vuota, ritorna None.
    """
    # Se None o stringa vuota/spazi, non c'è scadenza
    if s is None or str(s).strip() == '':                  # gestisce anche valori non-str accidentalmente
        return None                                        # nessuna data
    # Prova a fare il parse della data col formato richiesto
    try:                                                   # blocco di validazione
        datetime.strptime(s, '%Y-%m-%d')                   # solleva ValueError se non valida
        return s                                           # ritorna la stringa se valida
    except Exception:                                      # qualsiasi errore => data non valida
        return None                                        # normalizza a None


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
    # Normalizza il titolo: trim e collassa gli spazi multipli
    raw = (title or '')                                    # evita None
    stripped = raw.strip()                                 # rimuove spazi iniziali/finali
    parts = stripped.split()                               # split su qualsiasi whitespace
    norm_title = ' '.join(parts)                           # ricompone con singoli spazi
    # Se il titolo è vuoto dopo normalizzazione, solleva errore
    if norm_title == '':                                   # validazione minima
        raise ValueError('title vuoto')                    # segnala input scorretto
    # Clampa la priorità nel range [1,5]
    pr = max(1, min(5, int(priority)))                     # converte a int e limita l'intervallo
    # Prepara i tag: lista vuota se None
    tag_iter = tags if tags is not None else []            # evita di iterare su None
    # Normalizza ciascun tag: lower, strip, rimuovi vuoti
    norm_tags = []                                         # inizializza contenitore
    seen = set()                                           # per garantire unicità
    for t in tag_iter:                                     # scorre i tag forniti
        s = (str(t).strip().lower())                       # trim e minuscolo
        if not s:                                          # salta se vuoto dopo trim
            continue                                       # ignora tag vuoti
        if s in seen:                                      # evita duplicati preservando ordine
            continue                                       # ignora duplicati
        seen.add(s)                                        # marca come visto
        norm_tags.append(s)                                # aggiunge alla lista finale
    # Ordina alfabeticamente i tag come richiesto
    norm_tags = sorted(norm_tags)                          # ordina per determinismo
    # Normalizza la data di scadenza
    norm_due = parse_due(due)                              # valida/normalizza scadenza
    # Ritorna la tupla normalizzata
    return (norm_title, pr, norm_tags, norm_due)           # output aggregato


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
    # Calcola il totale dei task
    total = len(tasks)                                     # numero totale
    # Conta i task completati
    done_cnt = sum(1 for t in tasks if t.done)             # somma booleani True
    # Gli aperti sono il resto
    open_cnt = total - done_cnt                            # differenza tra totale e completati
    # Conta i tag aggregando su tutti i task (case-insensitive coerente con normalizzazione)
    by_tag: dict[str, int] = {}                            # mappa tag -> conteggio
    for t in tasks:                                        # scorre i task
        for tg in (t.tags or []):                          # iterazione sui tag presenti
            key = str(tg).lower()                          # uniforma a minuscolo
            by_tag[key] = by_tag.get(key, 0) + 1           # incrementa il contatore
    # Ritorna il report statistiche
    return {'total': total, 'open': open_cnt, 'done': done_cnt, 'by_tag': by_tag}  # struttura richiesta


# =============================================================
# M7) Export CSV
# =============================================================
def export_csv(tasks: list[Task], path: str) -> None:
    """Milestone 7: Esporta i task in CSV con header:
    id,title,priority,due,done,tags,created
    - 'tags' uniti da '|' (pipe) nell'ordine già presente.
    - UTF-8, newline=''
    """
    # Apre il file CSV per scrittura, newline='' per gestione corretta line endings
    with open(path, 'w', encoding='utf-8', newline='') as f:  # apre e sovrascrive
        writer = csv.writer(f)                              # istanzia writer CSV
        # Scrive l'intestazione nelle colonne richieste
        writer.writerow(['id', 'title', 'priority', 'due', 'done', 'tags', 'created'])  # header
        # Scrive una riga per ciascun task
        for t in tasks:                                     # iterazione sui task
            tag_field = '|'.join(t.tags or [])              # unisce i tag con pipe
            writer.writerow([t.id, t.title, t.priority, t.due, t.done, tag_field, t.created])  # riga dati


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
    # Costruisce il set di coppie (title_lower, due) già presenti
    existing = {(t.title.lower(), t.due) for t in tasks}    # per deduplicare
    # Trova l'ultimo id corrente per generare id successivi
    next_id = (max((t.id for t in tasks), default=0) + 1)   # prossimo id libero
    # Contatore di import effettivi
    imported = 0                                            # inizializza contatore
    # Apre e legge il CSV
    with open(path, 'r', encoding='utf-8') as f:            # apre il file CSV
        reader = csv.DictReader(f)                          # usa DictReader per nomi colonne
        for row in reader:                                  # scorre le righe
            # Estrae i campi base dal CSV
            raw_title = row.get('title', '')                # titolo grezzo
            raw_priority = row.get('priority', 3)           # priorità grezza
            raw_due = row.get('due', None)                  # scadenza grezza
            raw_done = row.get('done', 'False')             # stato grezzo come stringa
            raw_tags = row.get('tags', '')                  # tag grezzi 'a|b|c'
            # Converte i tag separati da '|' in lista
            tag_list = [p for p in raw_tags.split('|')] if raw_tags else []  # lista tag
            # Normalizza i campi secondo M5
            norm_title, pr, norm_tags, norm_due = normalize_task_fields(
                raw_title, int(raw_priority), tag_list, raw_due)             # normalizzazione input
            # Applica dedupe: confronta (title_lower, due) normalizzati
            sig = (norm_title.lower(), norm_due)             # firma per deduplicazione
            if sig in existing:                              # se già presente salta
                continue                                     # nessun import
            # Crea il nuovo Task con id progressivo
            t = Task(id=next_id, title=norm_title, priority=pr,
                     due=norm_due, done=str(raw_done).lower() in ('1','true','yes','y'),
                     tags=norm_tags, created=date.today().isoformat())       # costruisce il task importato
            # Aggiunge alla lista e aggiorna lo stato per dedupe successivo
            tasks.append(t)                                  # merge nella lista esistente
            existing.add(sig)                                # aggiorna set dedupe
            imported += 1                                    # incrementa contatore
            next_id += 1                                     # prepara id per eventuale prossimo
    # Ritorna quanti sono stati importati
    return imported                                         # numero di nuovi task


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
    # Prefisso di stato: [x] se done True, altrimenti [ ]
    status = '[x]' if t.done else '[ ]'                     # indica completamento
    # Base: id, priorità e titolo
    base = f"{status} #{t.id} (P{t.priority}) {t.title}"    # parte fissa della stringa
    # Parti opzionali: due e tags
    extras = []                                             # raccoglitore di segmenti opzionali
    if t.due:                                               # se la scadenza esiste
        extras.append(f"due {t.due}")                       # aggiunge la scadenza
    if t.tags:                                              # se sono presenti tag
        extras.append(f"tags: {','.join(t.tags)}")          # aggiunge i tag separati da virgola
    # Se ci sono extra, uniscili con " — "
    if extras:                                              # verifica presenza extra
        return base + " — " + " — ".join(extras)            # concatena base + extra
    # Altrimenti ritorna solo la base
    return base                                             # niente extra da mostrare


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
    # Se non fornita una cartella temporanea, creane una
    tmp = tmpdir or tempfile.mkdtemp(prefix='mini_todo_')   # directory temporanea di lavoro
    # Prepara una lista di task vuota
    tasks: list[Task] = []                                   # contenitore principale
    # Crea 3 task di esempio
    add_task(tasks, 'Task A', priority=2, tags=['lavoro'])   # primo task
    add_task(tasks, 'Task B', priority=5, due='2025-12-01')  # secondo con scadenza
    add_task(tasks, 'Task C', tags=['personale'])            # terzo con tag
    # Salva su JSON
    json_path = os.path.join(tmp, 'db.json')                 # percorso file json
    save_db(json_path, tasks)                                # persiste su disco
    # Ricarica dal JSON
    tasks_loaded = load_db(json_path)                        # legge quanto salvato
    # Esporta in CSV
    csv_path = os.path.join(tmp, 'export.csv')               # percorso file csv
    export_csv(tasks_loaded, csv_path)                       # esporta i task caricati
    # Re-importa (dovrebbe importare 0 per via dei duplicati)
    imported = import_csv(tasks_loaded, csv_path)            # merge con dedupe
    # Calcola le statistiche finali
    report = stats(tasks_loaded)                             # ottiene conteggi
    # Ritorna un riepilogo utile ai test
    return {                                                 # struttura di ritorno
        'counts': {'imported': imported, **report},          # merge importati + stats
        'paths': {'tmp': tmp, 'json': json_path, 'csv': csv_path}  # percorsi usati
    }                                                        # fine scenario


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
    print(f"\\n✅ Milestones superate: {passed}/{total}")
    if passed < total:
        for i, flag in enumerate(ok, start=1):
            if not flag:
                print(f"- M{i} FALLITA")
    else:
        print("Tutte le milestones superano i test. Ottimo lavoro!\\n")

if __name__ == '__main__':
    run_milestone_tests()
