# esercizio_04_compito_funzioni.py
# ============================================================
# 20 funzioni da implementare + test runner.
# I test sono pensati per dire chiaramente:
# - OK                 -> funzione corretta
# - FAIL               -> funzione implementata ma sbagliata
# - NON IMPLEMENTATA   -> funzione lascia NotImplementedError
#
# Regole:
# - NON usare librerie esterne.
# - Mantieni le firme (nome + parametri) invariate.
# - Leggi attentamente le docstring: sono la specifica!
# ============================================================

from __future__ import annotations
from typing import Any, Callable, Deque, Dict, Iterable, Iterator, List, Sequence, Tuple, TypeVar, Optional
from collections import deque, defaultdict
import math
import os
import re
import tempfile


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


# 1
def sum_even_numbers(nums: Iterable[int]) -> int:
    """
    Restituisce la somma di tutti i numeri PARI in `nums`.
    Esempio: [1,2,3,4] -> 6
    """
    raise NotImplementedError


# 2
def unique_words(text: str) -> set[str]:
    """
    Restituisce l'insieme di parole uniche in lowercase, rimuovendo punteggiatura semplice.
    Separatore: spazi. Punteggiatura da rimuovere: , . ; : ! ?
    Esempio: "Ciao, ciao! Mondo." -> {"ciao", "mondo"}
    """
    raise NotImplementedError


# 3
def safe_div(x: float, y: float) -> Optional[float]:
    """
    Divisione sicura: x / y.
    - Se y == 0 -> restituisci None (non lanciare eccezione).
    - Altrimenti il float del risultato.
    """
    raise NotImplementedError


# 4
def chunk_list(items: Sequence[T], size: int) -> List[List[T]]:
    """
    Partiziona `items` in blocchi consecutivi di lunghezza `size` (ultimo blocco può essere più corto).
    Esempio: [1,2,3,4,5], size=2 -> [[1,2],[3,4],[5]]
    Vincoli: size > 0, altrimenti ValueError.
    """
    raise NotImplementedError


# 5
def flatten(nested: Iterable[Iterable[T]]) -> List[T]:
    """
    Appiattisce una lista di liste (un solo livello).
    Esempio: [[1,2],[3],[4,5]] -> [1,2,3,4,5]
    """
    raise NotImplementedError


# 6
def frequency_counter(seq: Iterable[T]) -> Dict[T, int]:
    """
    Conta le occorrenze degli elementi di `seq` e restituisce un dict elemento->conteggio.
    """
    raise NotImplementedError


# 7
def merge_dicts_sum_values(a: Dict[K, int], b: Dict[K, int]) -> Dict[K, int]:
    """
    Unisce due dizionari sommando i valori per le chiavi in comune.
    Esempio: {a:1,b:2} + {b:3,c:4} -> {a:1,b:5,c:4}
    """
    raise NotImplementedError


# 8
def rotate_list(items: List[T], k: int) -> List[T]:
    """
    Ruota la lista a destra di k posizioni (k può essere > len).
    Esempio: [1,2,3,4], k=1 -> [4,1,2,3]
    """
    raise NotImplementedError


# 9
def is_anagram(a: str, b: str) -> bool:
    """
    True se `a` e `b` sono anagrammi ignorando spazi, maiuscole e punteggiatura semplice (,.;:!?).
    Esempio: "Dormitory" vs "Dirty room!" -> True
    """
    raise NotImplementedError


# 10
def normalize_whitespace(s: str) -> str:
    """
    Comprimi tutti gli spazi/whitespace (inclusi multiple line breaks) in SINGOLI spazi, e fai strip.
    Esempio: "  ciao   \n   mondo  " -> "ciao mondo"
    """
    raise NotImplementedError


# 11
def read_file_lines(path: str) -> List[str]:
    """
    Legge un file di testo e restituisce la lista delle righe SENZA newline finali.
    Se il file non esiste -> FileNotFoundError (propagare).
    """
    raise NotImplementedError


# 12
def tail(path: str, n: int) -> List[str]:
    """
    Restituisce le ULTIME n righe del file (senza newline finali).
    Vincoli: n >= 0, altrimenti ValueError.
    """
    raise NotImplementedError


# 13
def factorial(n: int) -> int:
    """
    Fattoriale iterativo.
    - n < 0 -> ValueError
    - factorial(0) = 1
    """
    raise NotImplementedError


# 14
def fibonacci(n: int) -> List[int]:
    """
    Restituisce i primi n numeri di Fibonacci a partire da 0,1.
    Esempio: n=6 -> [0,1,1,2,3,5]
    Vincoli: n >= 0, altrimenti ValueError.
    """
    raise NotImplementedError


# 15
def windowed(it: Iterable[T], size: int, step: int = 1) -> Iterator[Tuple[T, ...]]:
    """
    Finestra mobile su iterable.
    - Restituisce un iteratore di tuple consecutive di lunghezza `size`.
    - Avanzamento: `step`.
    - Se size <= 0 o step <= 0 -> ValueError.
    Esempio: list(windowed([1,2,3,4], size=3)) -> [(1,2,3),(2,3,4)]
    """
    raise NotImplementedError


# 16
def validate_email(s: str) -> bool:
    """
    Valida in modo SEMPLIFICATO una email (pattern basilare).
    Requisiti minimi:
      - una '@'
      - dominio con almeno un punto
      - nessun spazio
    Non serve coprire tutti i casi RFC.
    """
    raise NotImplementedError


# 17
def apply_strategy(nums: Iterable[int], fn: Callable[[int], int]) -> List[int]:
    """
    Applica la funzione `fn` a ogni intero in `nums` e restituisce la lista dei risultati.
    """
    raise NotImplementedError


# 18
def group_by(items: Iterable[T], key_fn: Callable[[T], K]) -> Dict[K, List[T]]:
    """
    Raggruppa `items` in un dict chiave->lista, dove la chiave è calcolata con `key_fn`.
    """
    raise NotImplementedError


# 19
def sort_points_by_distance(points: Iterable[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """
    Ordina i punti (x,y) per distanza dall'origine in ordine crescente.
    """
    raise NotImplementedError


# 20
def slugify(s: str) -> str:
    """
    Converte una stringa in 'slug' URL-friendly:
    - lowercase
    - caratteri alfanumerici e spazi/underscore
    - sostituisce sequenze di non-alfanumerici con '-'
    - comprime '-' ripetuti, fa strip dei '-'
    Esempio: "Hello,  World!!" -> "hello-world"
    """
    raise NotImplementedError


# ============================================================
# TEST RUNNER
# ============================================================

class _Result:
    def __init__(self, name: str, ok: bool, msg: str = ""):
        self.name = name
        self.ok = ok
        self.msg = msg

    def line(self) -> str:
        if self.msg == "NON IMPLEMENTATA":
            return f"[{self.name}] NON IMPLEMENTATA"
        return f"[{self.name}] {'OK' if self.ok else 'FAIL'}{(' - ' + self.msg) if self.msg else ''}"


def _expect_equal(name: str, got: Any, expected: Any) -> _Result:
    ok = (got == expected)
    return _Result(name, ok, "" if ok else f"atteso={expected!r}, ottenuto={got!r}")


def _catch_not_implemented(name: str, fn: Callable[[], Any], expected: Any = None, custom_check: Callable[[Any], bool] | None = None) -> _Result:
    try:
        value = fn()
        if custom_check is not None:
            ok = custom_check(value)
            return _Result(name, ok, "" if ok else f"check custom fallito. ottenuto={value!r}")
        if expected is not None:
            return _expect_equal(name, value, expected)
        return _Result(name, True, "")
    except NotImplementedError:
        return _Result(name, False, "NON IMPLEMENTATA")
    except AssertionError as e:
        return _Result(name, False, f"assertion: {e}")
    except Exception as e:
        return _Result(name, False, f"eccezione: {type(e).__name__}: {e}")


def _build_temp_file(lines: List[str]) -> str:
    fd, path = tempfile.mkstemp(prefix="compito_", suffix=".txt")
    os.close(fd)
    with open(path, "w", encoding="utf-8") as f:
        for i, line in enumerate(lines):
            f.write(line)
            if i < len(lines) - 1:
                f.write("\n")
    return path


def run_tests() -> None:
    results: List[_Result] = []

    # 1
    results.append(_catch_not_implemented(
        "sum_even_numbers",
        lambda: sum_even_numbers([1, 2, 3, 4, 6, 7, 8]),
        2 + 4 + 6 + 8
    ))

    # 2
    results.append(_catch_not_implemented(
        "unique_words",
        lambda: unique_words("Ciao, ciao! Mondo. ciao; Mondo?"),
        {"ciao", "mondo"}
    ))

    # 3
    results.append(_catch_not_implemented(
        "safe_div / ok",
        lambda: safe_div(9, 3),
        3.0
    ))
    results.append(_catch_not_implemented(
        "safe_div / by_zero",
        lambda: safe_div(5, 0),
        None
    ))

    # 4
    results.append(_catch_not_implemented(
        "chunk_list",
        lambda: chunk_list([1, 2, 3, 4, 5], 2),
        [[1, 2], [3, 4], [5]]
    ))

    # 5
    results.append(_catch_not_implemented(
        "flatten",
        lambda: flatten([[1, 2], [], [3], [4, 5]]),
        [1, 2, 3, 4, 5]
    ))

    # 6
    results.append(_catch_not_implemented(
        "frequency_counter",
        lambda: frequency_counter("abcaabb"),
        {"a": 3, "b": 3, "c": 1}
    ))

    # 7
    results.append(_catch_not_implemented(
        "merge_dicts_sum_values",
        lambda: merge_dicts_sum_values({"a": 1, "b": 2}, {"b": 3, "c": 4}),
        {"a": 1, "b": 5, "c": 4}
    ))

    # 8
    results.append(_catch_not_implemented(
        "rotate_list",
        lambda: rotate_list([1, 2, 3, 4], 1),
        [4, 1, 2, 3]
    ))
    results.append(_catch_not_implemented(
        "rotate_list / large k",
        lambda: rotate_list([1, 2, 3, 4], 6),
        [3, 4, 1, 2]
    ))

    # 9
    results.append(_catch_not_implemented(
        "is_anagram / true",
        lambda: is_anagram("Dormitory", "Dirty room!"),
        True
    ))
    results.append(_catch_not_implemented(
        "is_anagram / false",
        lambda: is_anagram("python", "typhon!x"),
        False
    ))

    # 10
    results.append(_catch_not_implemented(
        "normalize_whitespace",
        lambda: normalize_whitespace("  ciao   \n   mondo\t\t "),
        "ciao mondo"
    ))

    # 11 & 12 (creiamo un file temporaneo)
    tmp_path = _build_temp_file(["riga1", "riga2", "riga3", "riga4", "riga5"])
    results.append(_catch_not_implemented(
        "read_file_lines",
        lambda: read_file_lines(tmp_path),
        ["riga1", "riga2", "riga3", "riga4", "riga5"]
    ))
    results.append(_catch_not_implemented(
        "tail",
        lambda: tail(tmp_path, 2),
        ["riga4", "riga5"]
    ))

    # 13
    results.append(_catch_not_implemented(
        "factorial / base",
        lambda: factorial(0),
        1
    ))
    results.append(_catch_not_implemented(
        "factorial / n=6",
        lambda: factorial(6),
        720
    ))

    # 14
    results.append(_catch_not_implemented(
        "fibonacci / n=6",
        lambda: fibonacci(6),
        [0, 1, 1, 2, 3, 5]
    ))

    # 15
    results.append(_catch_not_implemented(
        "windowed",
        lambda: list(windowed([1, 2, 3, 4], size=3)),
        [(1, 2, 3), (2, 3, 4)]
    ))

    # 16
    results.append(_catch_not_implemented(
        "validate_email / true",
        lambda: validate_email("name.surname+tag@example.co.uk"),
        True
    ))
    results.append(_catch_not_implemented(
        "validate_email / false (no dot)",
        lambda: validate_email("user@example"),
        False
    ))
    results.append(_catch_not_implemented(
        "validate_email / false (space)",
        lambda: validate_email("user name@example.com"),
        False
    ))

    # 17
    results.append(_catch_not_implemented(
        "apply_strategy",
        lambda: apply_strategy([1, 2, 3], lambda x: x * x),
        [1, 4, 9]
    ))

    # 18
    results.append(_catch_not_implemented(
        "group_by",
        lambda: group_by(["cat", "car", "dog", "door"], key_fn=lambda s: s[0]),
        {"c": ["cat", "car"], "d": ["dog", "door"]}
    ))

    # 19
    results.append(_catch_not_implemented(
        "sort_points_by_distance",
        lambda: sort_points_by_distance([(3, 4), (0, 0), (1, 1)]),
        [(0, 0), (1, 1), (3, 4)]
    ))

    # 20
    results.append(_catch_not_implemented(
        "slugify",
        lambda: slugify("  Hello,  World!!  "),
        "hello-world"
    ))

    # Report
    total = len(results)
    ok_count = sum(1 for r in results if r.ok and r.msg != "NON IMPLEMENTATA")
    non_impl_count = sum(1 for r in results if r.msg == "NON IMPLEMENTATA")
    fail_count = total - ok_count - non_impl_count

    print("\n=== RISULTATI TEST ===")
    for r in results:
        print(r.line())
    print("======================")
    print(f"Totale: {total} | OK: {ok_count} | FAIL: {fail_count} | NON IMPLEMENTATE: {non_impl_count}")


if __name__ == "__main__":
    run_tests()
