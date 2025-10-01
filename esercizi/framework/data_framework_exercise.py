
# -*- coding: utf-8 -*-
"""
Esercizio: Framework di Analisi Dati Personalizzato
===================================================

Obiettivo
---------
Implementa una mini-libreria per manipolare dataset (liste di dizionari).
Il lavoro è suddiviso in milestone (M1..M8) con test automatici inclusi in questo stesso file.

Come usare
----------
1) Completa il codice nelle sezioni contrassegnate con "TODO (M#)".
2) Esegui il file da terminale:
     python data_framework_exercise.py
   Premi Invio quando richiesto: verranno lanciati i test e alla fine vedrai
   quante verifiche hai superato.
3) Lavora milestone per milestone: alla fine di ciascuna milestone, riesegui i test.

Argomenti toccati
-----------------
- Classi e oggetti, incapsulamento
- Metodi magici: __len__, __iter__, __getitem__
- Funzioni higher-order: map, filter, reduce
- Composizione e mixin (ExportJSON/CSV)
- Gestione eccezioni
- (Estensione facoltativa) ABC per processori dati

Convenzioni
-----------
- Non modificare la firma dei metodi richiesti.
- Mantieni immutabile il dataset di origine: i metodi che trasformano (filter/map)
  devono restituire un nuovo DataSet.
- Alza eccezioni chiare (ValueError/TypeError) quando indicato.
"""

from __future__ import annotations

from typing import Callable, Iterable, Iterator, List, Dict, Any, Optional, Union
from functools import reduce as _py_reduce
import json, csv, os

# ======================
#       CORE API
# ======================

class DataSet:
    """
    Rappresenta una collezione di record (dizionari).

    Requisiti:
    - Deve contenere una lista di dict (List[Dict[str, Any]]). (M1)
    - Supporta len(), iterazione, indicizzazione. (M2)
    - Espone metodi:
      * filter(predicate) -> DataSet  (M3)
      * map(transform) -> DataSet      (M4)
      * reduce(func, initial) -> Any   (M5)
      * group_by(key_or_fn) -> Dict[Any, 'DataSet'] (M6)
      * sum(field), mean(field), min(field), max(field) (M7)
    - Esporta su file via mixin (M8) – vedi classi ExportJSONMixin / ExportCSVMixin.
    """

    def __init__(self, rows: List[Dict[str, Any]]):
        # TODO (M1): Validare il tipo di rows e che ogni elemento sia un dict.
        # - Se rows non è una lista di dizionari: alza ValueError
        # - Memorizza internamente una *copia superficiale* dei dati
        raise NotImplementedError("TODO M1")

    # ---------- Metodi magici (M2) ----------
    def __len__(self) -> int:
        # TODO (M2): Restituisci la lunghezza del dataset
        raise NotImplementedError("TODO M2")

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        # TODO (M2): Rendi il dataset iterabile sui record
        raise NotImplementedError("TODO M2")

    def __getitem__(self, index: int) -> Dict[str, Any]:
        # TODO (M2): Permetti l'accesso indicizzato
        raise NotImplementedError("TODO M2")

    # ---------- Operazioni funzionali ----------
    def filter(self, predicate: Callable[[Dict[str, Any]], bool]) -> 'DataSet':
        """Ritorna un nuovo DataSet con i record per cui predicate(record) è True. (M3)"""
        # TODO (M3): Implementa filter
        raise NotImplementedError("TODO M3")

    def map(self, transform: Callable[[Dict[str, Any]], Dict[str, Any]]) -> 'DataSet':
        """Ritorna un nuovo DataSet con record trasformati da transform(record). (M4)

        NOTE:
        - transform deve restituire un dict. Se non lo fa, alza TypeError.
        """
        # TODO (M4): Implementa map
        raise NotImplementedError("TODO M4")

    def reduce(self, func: Callable[[Any, Dict[str, Any]], Any], initial: Any) -> Any:
        """Riduce i record ad un unico valore usando func(acc, rec), partendo da initial. (M5)"""
        # TODO (M5): Implementa reduce (puoi usare functools.reduce)
        raise NotImplementedError("TODO M5")

    # ---------- Raggruppamenti e aggregazioni ----------
    def group_by(self, key_or_fn: Union[str, Callable[[Dict[str, Any]], Any]]) -> Dict[Any, 'DataSet']:
        """
        Raggruppa i record per chiave (nome campo) o per funzione di key. (M6)

        Esempi:
            ds.group_by('city') -> { 'Rome': DataSet([...]), 'Milan': DataSet([...]) }
            ds.group_by(lambda r: r['age'] // 10) -> { 2: DataSet([...]), 3: DataSet([...]) }
        """
        # TODO (M6): Implementa group_by
        raise NotImplementedError("TODO M6")

    def _numeric_series(self, field: str) -> List[float]:
        """Estrae i valori numerici dal campo richiesto, alzando errori sensati. (M7 helper)"""
        # TODO (M7): Implementa estrazione e validazioni:
        # - Se il campo non esiste in almeno un record -> ValueError
        # - Se un valore non è numerico -> TypeError
        raise NotImplementedError("TODO M7")

    def sum(self, field: str) -> float:
        # TODO (M7): Somma dei valori numerici del campo
        raise NotImplementedError("TODO M7")

    def mean(self, field: str) -> float:
        # TODO (M7): Media dei valori numerici del campo (gestisci dataset vuoto con ValueError)
        raise NotImplementedError("TODO M7")

    def min(self, field: str) -> float:
        # TODO (M7): Minimo dei valori numerici del campo
        raise NotImplementedError("TODO M7")

    def max(self, field: str) -> float:
        # TODO (M7): Massimo dei valori numerici del campo
        raise NotImplementedError("TODO M7")


# ======================
#         MIXIN
# ======================

class ExportJSONMixin:
    """Mixin per esportare il dataset in JSON (M8)."""
    def export_json(self, path: str, *, indent: int = 2) -> None:
        # TODO (M8): Scrivi i record del dataset in JSON su 'path'
        raise NotImplementedError("TODO M8")


class ExportCSVMixin:
    """Mixin per esportare il dataset in CSV (M8).
    - Le colonne sono l'unione delle chiavi presenti nei record, in ordine alfabetico.
    """
    def export_csv(self, path: str) -> None:
        # TODO (M8): Scrivi i record in CSV su 'path'
        raise NotImplementedError("TODO M8")


# ======================
#   IMPLEMENTAZIONE FINALE
#   (lo studente può decidere se ereditare i mixin)
# ======================

class ExportableDataSet(ExportJSONMixin, ExportCSVMixin, DataSet):
    """DataSet + mixin di export (M8)."""
    pass


# ======================
#         TESTS
# ======================

_SAMPLE = [
    {"name": "Alice", "age": 30, "city": "Rome", "salary": 3200.0},
    {"name": "Bob",   "age": 24, "city": "Milan", "salary": 2800.0},
    {"name": "Cecilia","age": 24, "city": "Rome", "salary": 3000.0},
    {"name": "Diego", "age": 41, "city": "Turin", "salary": 4100.0},
]

class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.logs: List[str] = []

    def _ok(self, msg: str):
        self.passed += 1
        self.logs.append(f"✔ {msg}")

    def _ko(self, msg: str, err: Exception):
        self.failed += 1
        self.logs.append(f"✘ {msg} -> {type(err).__name__}: {err}")

    def run(self):
        print("Esecuzione test...")

        # ------- M1 -------
        try:
            ds = DataSet(_SAMPLE)
            self._ok("M1: __init__ accetta lista di dict")
        except Exception as e:
            self._ko("M1: __init__ accetta lista di dict", e)

        try:
            DataSet([1,2,3])
            self._ko("M1: __init__ valida tipi errati", Exception("mancata eccezione"))
        except ValueError:
            self._ok("M1: __init__ valida tipi errati")
        except Exception as e:
            self._ko("M1: __init__ valida tipi errati (tipo errato di eccezione)", e)

        # ------- M2 -------
        try:
            ds = DataSet(_SAMPLE)
            assert len(ds) == 4
            it = iter(ds)
            first = next(it)
            assert isinstance(first, dict)
            assert ds[1]["name"] == "Bob"
            self._ok("M2: __len__/__iter__/__getitem__")
        except Exception as e:
            self._ko("M2: __len__/__iter__/__getitem__", e)

        # ------- M3 -------
        try:
            ds = DataSet(_SAMPLE)
            adults = ds.filter(lambda r: r["age"] >= 30)
            assert len(adults) == 2
            # immutabilità
            assert len(ds) == 4
            self._ok("M3: filter() mantiene immutabilità e filtra correttamente")
        except Exception as e:
            self._ko("M3: filter()", e)

        # ------- M4 -------
        try:
            ds = DataSet(_SAMPLE)
            up = ds.map(lambda r: {"NAME": r["name"].upper(), **r})
            assert isinstance(up[0], dict) and "NAME" in up[0]
            # errore se transform non ritorna dict
            try:
                ds.map(lambda r: 123)  # deve fallire
                self._ko("M4: map() valida output transform", Exception("mancata eccezione"))
            except TypeError:
                pass
            self._ok("M4: map() trasforma record e valida tipo")
        except Exception as e:
            self._ko("M4: map()", e)

        # ------- M5 -------
        try:
            ds = DataSet(_SAMPLE)
            total = ds.reduce(lambda acc, r: acc + r["salary"], 0.0)
            assert abs(total - (3200.0+2800.0+3000.0+4100.0)) < 1e-6
            self._ok("M5: reduce() aggrega valori")
        except Exception as e:
            self._ko("M5: reduce()", e)

        # ------- M6 -------
        try:
            ds = DataSet(_SAMPLE)
            by_city = ds.group_by("city")
            assert set(by_city.keys()) == {"Rome","Milan","Turin"}
            assert len(by_city["Rome"]) == 2
            by_age_decade = ds.group_by(lambda r: r["age"] // 10)
            assert set(by_age_decade.keys()) == {2,3,4}
            self._ok("M6: group_by() per chiave o funzione")
        except Exception as e:
            self._ko("M6: group_by()", e)

        # ------- M7 -------
        try:
            ds = DataSet(_SAMPLE)
            assert ds.sum("salary") == 13100.0
            assert round(ds.mean("salary"), 2) == 3275.0
            assert ds.min("age") == 24
            assert ds.max("age") == 41
            # errori sensati
            try:
                ds.sum("missing")
                self._ko("M7: aggregazioni su campo mancante", Exception("mancata eccezione"))
            except ValueError:
                pass
            bad = DataSet([{"age": "not-a-number"}])
            try:
                bad.sum("age")
                self._ko("M7: aggregazioni su valori non numerici", Exception("mancata eccezione"))
            except TypeError:
                pass
            self._ok("M7: aggregazioni numeriche e validazioni")
        except Exception as e:
            self._ko("M7: aggregazioni", e)

        # ------- M8 -------
        try:
            ds = ExportableDataSet(_SAMPLE)
            json_path = "out_dataset.json"
            csv_path = "out_dataset.csv"
            ds.export_json(json_path)
            ds.export_csv(csv_path)
            assert os.path.exists(json_path) and os.path.getsize(json_path) > 0
            assert os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
            # cleanup
            os.remove(json_path)
            os.remove(csv_path)
            self._ok("M8: export JSON/CSV")
        except Exception as e:
            self._ko("M8: export JSON/CSV", e)

        print("\nRisultati:")
        for line in self.logs:
            print(line)
        print(f"\nTotale: {self.passed + self.failed}  |  Superati: {self.passed}  |  Falliti: {self.failed}")
        return self.passed, self.failed


if __name__ == "__main__":
    input("Premi Invio per eseguire i test...")
    runner = TestRunner()
    ok, ko = runner.run()
    if ko == 0:
        print("\n\u2705 Tutti i test superati! Procedi alla milestone successiva o fai refactoring.")
    else:
        print("\n\u26A0\uFE0F Alcuni test non sono passati. Completa le TODO e riprova.")
