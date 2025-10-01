"""
Soluzioni — Generatori e Slicing
Due stili per ogni funzione:
1) Versione pythonic corretta
2) Nei commenti: versione "vecchia maniera"
"""

# =====================
# SEZIONE SOLUZIONI
# =====================

# 1) Slicing di base
def primi_tre_elementi(seq: list[int]) -> list[int]:
    # Versione Pythonic
    return seq[:3]

    # Versione "vecchia maniera"
    # out = []
    # count = 0
    # for x in seq:
    #     if count == 3:
    #         break
    #     out.append(x)
    #     count += 1
    # return out


# 2) Ultimi elementi
def ultimi_due(seq: list[int]) -> list[int]:
    # Versione Pythonic
    return seq[-2:]

    # Versione "vecchia maniera"
    # n = len(seq)
    # if n == 0:
    #     return []
    # if n == 1:
    #     return [seq[0]]
    # return [seq[n-2], seq[n-1]]


# 3) Lista invertita
def inverti(seq: list[int]) -> list[int]:
    # Versione Pythonic
    return seq[::-1]

    # Versione "vecchia maniera"
    # out = []
    # i = len(seq) - 1
    # while i >= 0:
    #     out.append(seq[i])
    #     i -= 1
    # return out


# 4) Elementi pari con slicing
def elementi_pari(seq: list[int]) -> list[int]:
    # Versione Pythonic
    return seq[0::2]

    # Versione "vecchia maniera"
    # out = []
    # i = 0
    # for x in seq:
    #     if i % 2 == 0:
    #         out.append(x)
    #     i += 1
    # return out


# 5) Generatore numeri
def genera_numeri(n: int):
    # Versione Pythonic
    for i in range(n):
        yield i

    # Versione "vecchia maniera"
    # i = 0
    # while i < n:
    #     yield i
    #     i += 1


# 6) Generatore quadrati
def quadrati(n: int):
    # Versione Pythonic
    for i in range(n):
        yield i * i

    # Versione "vecchia maniera"
    # i = 0
    # while i < n:
    #     yield i * i
    #     i += 1


# 7) Generatore infiniti pari
def infiniti_pari():
    # Versione Pythonic
    x = 0
    while True:
        yield x
        x += 2

    # Versione "vecchia maniera"
    # x = 0
    # while True:
    #     yield x
    #     x = x + 2


# 8) Finestra scorrevole con slicing
def finestre(seq: list[int], k: int) -> list[list[int]]:
    # Versione Pythonic
    if k <= 0 or k > len(seq):
        return [] if k <= 0 else [seq[:]] if k == len(seq) else []
    return [seq[i:i + k] for i in range(len(seq) - k + 1)]

    # Versione "vecchia maniera"
    # if k <= 0:
    #     return []
    # n = len(seq)
    # out = []
    # i = 0
    # while i + k <= n:
    #     blocco = []
    #     j = i
    #     # copia manuale degli elementi
    #     while j < i + k:
        #         blocco.append(seq[j])
    #         j += 1
    #     out.append(blocco)
    #     i += 1
    # return out


# 9) Generatore Fibonacci
def fibonacci(n: int):
    # Versione Pythonic
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

    # Versione "vecchia maniera"
    # a = 0
    # b = 1
    # count = 0
    # while count < n:
    #     yield a
    #     temp = a + b
    #     a = b
    #     b = temp
    #     count += 1


# 10) Generatore numeri primi
def primi(n: int):
    # Versione Pythonic
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        r = int(x ** 0.5)
        return all(x % d for d in range(3, r + 1, 2))

    found = 0
    cand = 2
    while found < n:
        if is_prime(cand):
            yield cand
            found += 1
        cand += 1


# =====================
# SEZIONE TEST (identica alla traccia)
# =====================

import unittest

class TestEsercizi(unittest.TestCase):
    def test_1(self):
        self.assertEqual(primi_tre_elementi([1,2,3,4]), [1,2,3])
        self.assertEqual(primi_tre_elementi([9]), [9])

    def test_2(self):
        self.assertEqual(ultimi_due([5,6,7,8]), [7,8])
        self.assertEqual(ultimi_due([1]), [1])

    def test_3(self):
        self.assertEqual(inverti([1,2,3]), [3,2,1])
        self.assertEqual(inverti([]), [])

    def test_4(self):
        self.assertEqual(elementi_pari([10,11,12,13,14]), [10,12,14])
        self.assertEqual(elementi_pari([1,2,3,4,5,6]), [1,3,5])

    def test_5(self):
        self.assertEqual(list(genera_numeri(3)), [0,1,2])

    def test_6(self):
        self.assertEqual(list(quadrati(4)), [0,1,4,9])

    def test_7(self):
        g = infiniti_pari()
        valori = [next(g) for _ in range(5)]
        self.assertEqual(valori, [0,2,4,6,8])

    def test_8(self):
        self.assertEqual(finestre([1,2,3,4],2), [[1,2],[2,3],[3,4]])
        self.assertEqual(finestre([1,2,3],3), [[1,2,3]])

    def test_9(self):
        self.assertEqual(list(fibonacci(5)), [0,1,1,2,3])

    def test_10(self):
        self.assertEqual(list(primi(5)), [2,3,5,7,11])


def _run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestEsercizi)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    passed = result.testsRun - len(result.failures) - len(result.errors)
    print()
    print("Risultato")
    print(f"Test eseguiti {result.testsRun}")
    print(f"Superati {passed}")
    print(f"Falliti {len(result.failures)}")
    print(f"Errori {len(result.errors)}")


if __name__ == "__main__":
    _run_tests()
