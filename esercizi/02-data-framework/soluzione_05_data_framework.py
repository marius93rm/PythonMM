# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Callable, Iterator, List, Dict, Any, Union
from functools import reduce as _py_reduce
import json, csv, os

# ======================
#       CORE API
# ======================

class DataSet:
    def __init__(self, rows: List[Dict[str, Any]]):
        # M1: validazione
        if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
            raise ValueError("rows deve essere una lista di dizionari")
        # copia superficiale
        self._rows = list(rows)

    # ---------- Metodi magici (M2) ----------
    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        return iter(self._rows)

    def __getitem__(self, index: int) -> Dict[str, Any]:
        return self._rows[index]

    # ---------- Operazioni funzionali ----------
    def filter(self, predicate: Callable[[Dict[str, Any]], bool]) -> 'DataSet':
        return DataSet([r for r in self._rows if predicate(r)])

    def map(self, transform: Callable[[Dict[str, Any]], Dict[str, Any]]) -> 'DataSet':
        new_rows = []
        for r in self._rows:
            tr = transform(r)
            if not isinstance(tr, dict):
                raise TypeError("transform deve restituire un dict")
            new_rows.append(tr)
        return DataSet(new_rows)

    def reduce(self, func: Callable[[Any, Dict[str, Any]], Any], initial: Any) -> Any:
        return _py_reduce(func, self._rows, initial)

    # ---------- Raggruppamenti e aggregazioni ----------
    def group_by(self, key_or_fn: Union[str, Callable[[Dict[str, Any]], Any]]) -> Dict[Any, 'DataSet']:
        groups: Dict[Any, List[Dict[str, Any]]] = {}
        for r in self._rows:
            if isinstance(key_or_fn, str):
                if key_or_fn not in r:
                    raise ValueError(f"Campo {key_or_fn} mancante")
                k = r[key_or_fn]
            else:
                k = key_or_fn(r)
            groups.setdefault(k, []).append(r)
        return {k: DataSet(v) for k, v in groups.items()}

    def _numeric_series(self, field: str) -> List[float]:
        values = []
        for r in self._rows:
            if field not in r:
                raise ValueError(f"Campo {field} mancante in un record")
            v = r[field]
            if not isinstance(v, (int, float)):
                raise TypeError(f"Valore non numerico trovato: {v}")
            values.append(float(v))
        return values

    def sum(self, field: str) -> float:
        vals = self._numeric_series(field)
        return sum(vals)

    def mean(self, field: str) -> float:
        vals = self._numeric_series(field)
        if not vals:
            raise ValueError("Dataset vuoto")
        return sum(vals) / len(vals)

    def min(self, field: str) -> float:
        vals = self._numeric_series(field)
        return min(vals)

    def max(self, field: str) -> float:
        vals = self._numeric_series(field)
        return max(vals)


# ======================
#         MIXIN
# ======================

class ExportJSONMixin:
    def export_json(self, path: str, *, indent: int = 2) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._rows, f, indent=indent, ensure_ascii=False)


class ExportCSVMixin:
    def export_csv(self, path: str) -> None:
        # colonne = unione di tutte le chiavi
        all_keys = sorted({k for r in self._rows for k in r.keys()})
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=all_keys)
            writer.writeheader()
            for r in self._rows:
                writer.writerow(r)


# ======================
#   IMPLEMENTAZIONE FINALE
# ======================

class ExportableDataSet(ExportJSONMixin, ExportCSVMixin, DataSet):
    pass
