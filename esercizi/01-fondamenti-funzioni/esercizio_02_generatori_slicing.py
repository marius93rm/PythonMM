"""
Esercizi su Generatori e Slicing
Difficoltà crescente — 10 esercizi
Implementa i TODO senza modificare la sezione TEST
Output pulito anche in caso di eccezioni
"""

# =====================
# SEZIONE ESERCIZI
# =====================

# 1) Slicing di base
def primi_tre_elementi(seq: list[int]) -> list[int]:
    """
    Ritorna i primi tre elementi della sequenza tramite slicing.
    Se la lista ha meno di 3 elementi, ritorna tutti quelli disponibili.
    Esempio: [1,2,3,4] -> [1,2,3]
    """
    # TODO
    raise NotImplementedError


# 2) Ultimi elementi
def ultimi_due(seq: list[int]) -> list[int]:
    """
    Ritorna gli ultimi due elementi tramite slicing.
    Esempio: [5,6,7,8] -> [7,8]
    """
    # TODO
    raise NotImplementedError


# 3) Lista invertita
def inverti(seq: list[int]) -> list[int]:
    """
    Ritorna la lista invertita usando slicing con step negativo.
    Esempio: [1,2,3] -> [3,2,1]
    """
    # TODO
    raise NotImplementedError


# 4) Elementi pari con slicing
def elementi_pari(seq: list[int]) -> list[int]:
    """
    Ritorna solo gli elementi in posizione pari (indici 0,2,4...).
    Usa slicing con step.
    Esempio: [10,11,12,13,14] -> [10,12,14]
    """
    # TODO
    raise NotImplementedError


# 5) Generatore numeri
def genera_numeri(n: int):
    """
    Genera i numeri da 0 a n-1 usando yield.
    Esempio: n=3 -> 0,1,2
    """
    # TODO
    raise NotImplementedError


# 6) Generatore quadrati
def quadrati(n: int):
    """
    Genera i quadrati dei numeri da 0 a n-1.
    Esempio: n=4 -> 0,1,4,9
    """
    # TODO
    raise NotImplementedError


# 7) Generatore infiniti pari
def infiniti_pari():
    """
    Generatore infinito dei numeri pari: 0,2,4,6...
    Usa yield in un ciclo while True.
    Suggerimento: serve test con break.
    """
    # TODO
    raise NotImplementedError


# 8) Finestra scorrevole con slicing
def finestre(seq: list[int], k: int) -> list[list[int]]:
    """
    Ritorna tutte le sottoliste consecutive di lunghezza k usando slicing.
    Esempio: [1,2,3,4], k=2 -> [[1,2],[2,3],[3,4]]
    """
    # TODO
    raise NotImplementedError


# 9) Generatore Fibonacci
def fibonacci(n: int):
    """
    Genera i primi n numeri di Fibonacci.
    Sequenza: 0,1,1,2,3,5,8...
    Esempio: n=5 -> 0,1,1,2,3
    """
    # TODO
    raise NotImplementedError


# 10) Generatore numeri primi
def primi(n: int):
    """
    Genera i primi n numeri primi.
    Esempio: n=5 -> 2,3,5,7,11
    Suggerimento: usa una funzione helper is_prime(x).
    """
    # TODO
    raise NotImplementedError


# =====================
# SEZIONE TEST AUTOMATICI CON GESTIONE ECCEZIONI
# =====================

def _safe_call(func, *args, expect=None, cmp=None):
    """
    Esegue func(*args) in sicurezza.
    Ritorna True se il risultato è uguale a expect secondo cmp, altrimenti False.
    Non stampa traceback in caso di errore, restituisce False.
    """
    try:
        res = func(*args)
        if cmp is None:
            return res == expect
        return cmp(res, expect)
    except Exception:
        return False


def _eq_list(a, b):
    return a == b


def _eq_iterable_list(iterable, expect_list):
    try:
        return list(iterable) == expect_list
    except Exception:
        return False


def _tests():
    tests = []

    # 1
    tests.append(_safe_call(primi_tre_elementi, [1,2,3,4], expect=[1,2,3], cmp=_eq_list))
    tests.append(_safe_call(primi_tre_elementi, [9], expect=[9], cmp=_eq_list))

    # 2
    tests.append(_safe_call(ultimi_due, [5,6,7,8], expect=[7,8], cmp=_eq_list))
    tests.append(_safe_call(ultimi_due, [1], expect=[1], cmp=_eq_list))

    # 3
    tests.append(_safe_call(inverti, [1,2,3], expect=[3,2,1], cmp=_eq_list))
    tests.append(_safe_call(inverti, [], expect=[], cmp=_eq_list))

    # 4
    tests.append(_safe_call(elementi_pari, [10,11,12,13,14], expect=[10,12,14], cmp=_eq_list))
    tests.append(_safe_call(elementi_pari, [1,2,3,4,5,6], expect=[1,3,5], cmp=_eq_list))

    # 5
    tests.append(_safe_call(genera_numeri, 3, expect=[0,1,2], cmp=_eq_iterable_list))

    # 6
    tests.append(_safe_call(quadrati, 4, expect=[0,1,4,9], cmp=_eq_iterable_list))

    # 7
    def _kill_after_5(gen_func):
        try:
            g = gen_func()
            vals = [next(g) for _ in range(5)]
            return vals == [0,2,4,6,8]
        except Exception:
            return False
    tests.append(_kill_after_5(infiniti_pari))

    # 8
    tests.append(_safe_call(finestre, [1,2,3,4], 2, expect=[[1,2],[2,3],[3,4]], cmp=_eq_list))
    tests.append(_safe_call(finestre, [1,2,3], 3, expect=[[1,2,3]], cmp=_eq_list))

    # 9
    tests.append(_safe_call(fibonacci, 5, expect=[0,1,1,2,3], cmp=_eq_iterable_list))

    # 10
    tests.append(_safe_call(primi, 5, expect=[2,3,5,7,11], cmp=_eq_iterable_list))

    return tests


def _run():
    results = _tests()
    eseguiti = len(results)
    superati = sum(1 for ok in results if ok)
    falliti = eseguiti - superati

    print(f"test eseguiti {eseguiti}")
    print(f"test superati {superati}")
    print(f"test falliti {falliti}")


if __name__ == "__main__":
    _run()
