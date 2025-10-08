"""
Esercizi Python giorno 1
Argomenti
funzioni, if, for, while, match case, walrus, liste, tuple, set, dizionari, built in

Istruzioni
Implementa i TODO senza modificare i test. Lancia il file per eseguire i test e vedere il report.
Scrivi codice chiaro e mantenibile.
"""

from __future__ import annotations
from typing import Iterable, Iterator, Any
import unittest


# 1. Pulizia anagrafica di base
def pulisci_nomi_clienti(nomi: list[str]) -> list[str]:
    """
    Dato un elenco di nomi e cognomi con spazi in eccesso e maiuscole a caso
    pulisci e normalizza

    Requisiti
    - rimuovi spazi agli estremi
    - comprimi spazi interni multipli in uno solo
    - porta tutto in formato Nome Cognome con iniziali maiuscole
    - rimuovi duplicati mantenendo il primo incontro

    Suggerimenti
    - usa split e join per gli spazi
    - usa title per le iniziali
    - per i duplicati puoi usare un set di visti

    Esempio
    ["  anna   rossi ", "Anna rossi", "MARCO  bianchi"] -> ["Anna Rossi", "Marco Bianchi"]
    """
    # TODO: implementa
    raise NotImplementedError


# 2. Valutazione password essenziali
def password_valide(passwords: Iterable[str]) -> set[str]:
    """
    Seleziona le password che rispettano queste regole minime di buon senso
    - lunghezza almeno 8
    - contiene almeno una lettera
    - contiene almeno una cifra

    Ritorna un set con le password valide

    Suggerimenti
    - any(ch.isalpha()) e any(ch.isdigit())
    - valuta anche casi limite come stringhe vuote
    """
    # TODO: implementa
    raise NotImplementedError


# 3. Analisi accessi di servizio
def conteggia_accessi_ok(log: list[tuple[str, int]]) -> dict[str, int]:
    """
    Dato un log come lista di tuple (utente, status)
    conta per ogni utente quante risposte sono state 200

    Requisiti
    - ritorna un dizionario utente -> conteggio di status 200
    - utenti senza 200 non compaiono

    Esempio
    [("anna", 200), ("anna", 500), ("marco", 200)] -> {"anna": 1, "marco": 1}
    """
    # TODO: implementa
    raise NotImplementedError


# 4. Media pesata dei voti
def media_pesata(voti: dict[str, tuple[int, int]]) -> float:
    """
    Calcola la media pesata dei voti
    La struttura è materia -> (voto, crediti)

    Requisiti
    - ritorna 0.0 se non ci sono crediti
    - usa built in come sum

    Esempio
    {"matematica": (30, 6), "storia": (27, 3)} -> (30*6 + 27*3) diviso (6 + 3)
    """
    # TODO: implementa
    raise NotImplementedError


# 5. Normalizzazione inventario
def unisci_inventari(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """
    Unisci due inventari sommando le quantità prodotto per prodotto

    Requisiti
    - non modificare i dizionari di input
    - se un prodotto è in uno solo dei due rimane con il suo valore
    - valori negativi sono ammessi e vanno sommati normalmente

    Esempio
    {"mela": 2, "pera": 1} e {"mela": 3, "kiwi": 5} -> {"mela": 5, "pera": 1, "kiwi": 5}
    """
    # TODO: implementa
    raise NotImplementedError


# 6. Pianificazione con priorità usando match case
def punteggio_priorita(etichetta: str) -> int:
    """
    Assegna un punteggio di priorità a una etichetta testuale

    Mappa prevista
    - "critica"   -> 3
    - "alta"      -> 2
    - "media"     -> 1
    - "bassa"     -> 0
    - qualunque altra -> 0

    Usa match case introdotto in Python 3.10
    """
    # TODO: implementa con match
    raise NotImplementedError


def ordina_task_per_priorita(task: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """
    Dato un elenco di task come (titolo, etichetta_priorita) ordina decrescendo per priorità
    In caso di pari punteggio ordina alfabeticamente per titolo

    Esempio
    [("backup", "alta"), ("patch", "critica"), ("report", "media")]
    -> [("patch", "critica"), ("backup", "alta"), ("report", "media")]
    """
    # TODO: implementa usando punteggio_priorita come key
    raise NotImplementedError


# 7. Bilancio mensile semplice
def riepilogo_bilancio(transazioni: list[dict[str, Any]]) -> dict[str, float]:
    """
    Ogni transazione ha campi
    {"categoria": str, "importo": float, "tipo": "entrata" oppure "uscita"}

    Requisiti
    - ritorna un dizionario con chiavi
      "totale_entrate", "totale_uscite", "saldo", "per_categoria"
    - "per_categoria" è un sotto dizionario categoria -> somma importi con segno
      per le uscite usa importi negativi

    Suggerimenti
    - somma con for o con comprensioni
    - attenzione alle categorie mai viste prima
    """
    # TODO: implementa
    raise NotImplementedError


# 8. Estrazione di parole chiave
def estrai_keyword(testi: Iterable[str], stopwords: set[str], minimo: int = 4) -> set[str]:
    """
    Dato un insieme di testi estrai parole chiave semplici

    Requisiti
    - normalizza a minuscolo
    - tieni solo parole alfanumeriche
    - rimuovi stopwords
    - tieni solo parole con lunghezza almeno pari a minimo

    Ritorna un set di keyword

    Suggerimenti
    - usa split e str.isalnum per un filtro basilare
    - un set evita duplicati
    """
    # TODO: implementa
    raise NotImplementedError


# 9. Ricerca con walrus operator
def primo_quadrato_maggiore_di(numeri: list[int], soglia: int) -> tuple[int, int] | None:
    """
    Ritorna una tupla con valore e indice del primo numero il cui quadrato supera la soglia
    Se nessun elemento soddisfa la condizione ritorna None

    Sfida
    - usa il walrus operator per evitare di ricalcolare il quadrato
    """
    # TODO: implementa con walrus
    raise NotImplementedError


# 10. Gruppi di anagrammi
def raggruppa_anagrammi(parole: Iterable[str]) -> dict[tuple[str, ...], list[str]]:
    """
    Raggruppa parole che sono anagrammi tra loro

    Requisiti
    - normalizza a minuscolo
    - la chiave del gruppo è una tupla di lettere ordinate in modo crescente
    - l ordine interno di ogni lista deve seguire l ordine di arrivo

    Esempio
    ["Roma", "amor", "ramo", "cane"] produce due gruppi
    chiave ("a","m","o","r") valore ["Roma", "amor", "ramo"]
    chiave ("a","c","e","n") valore ["cane"]
    """
    # TODO: implementa
    raise NotImplementedError


# -----------------------
#           TEST
# -----------------------

class TestEserciziGiorno1(unittest.TestCase):
    def test_01_pulisci_nomi_clienti(self):
        dati = ["  anna   rossi ", "Anna rossi", "MARCO  bianchi", "marco bianchi", " giulia Verdi "]
        out = pulisci_nomi_clienti(dati)
        self.assertEqual(out, ["Anna Rossi", "Marco Bianchi", "Giulia Verdi"])

    def test_02_password_valide(self):
        pw = ["abcd1234", "AAAAAA11", "short7", "", "sololettere", "12345678", "Mix987xyz"]
        valid = password_valide(pw)
        self.assertEqual(valid, {"abcd1234", "AAAAAA11", "Mix987xyz"})

    def test_03_conteggia_accessi_ok(self):
        log = [("anna", 200), ("anna", 500), ("marco", 200), ("anna", 200), ("luca", 404)]
        self.assertEqual(conteggia_accessi_ok(log), {"anna": 2, "marco": 1})

    def test_04_media_pesata(self):
        voti = {"matematica": (30, 6), "storia": (27, 3), "arte": (18, 0)}
        self.assertAlmostEqual(media_pesata(voti), (30*6 + 27*3) / 9)
        self.assertEqual(media_pesata({}), 0.0)
        self.assertEqual(media_pesata({"arte": (25, 0)}), 0.0)

    def test_05_unisci_inventari(self):
        a = {"mela": 2, "pera": 1}
        b = {"mela": 3, "kiwi": 5}
        out = unisci_inventari(a, b)
        self.assertEqual(out, {"mela": 5, "pera": 1, "kiwi": 5})
        self.assertEqual(a, {"mela": 2, "pera": 1})
        self.assertEqual(b, {"mela": 3, "kiwi": 5})
        c = {"vite": -2}
        d = {"vite": 5}
        self.assertEqual(unisci_inventari(c, d), {"vite": 3})

    def test_06_priorita_match_case(self):
        self.assertEqual(punteggio_priorita("critica"), 3)
        self.assertEqual(punteggio_priorita("alta"), 2)
        self.assertEqual(punteggio_priorita("media"), 1)
        self.assertEqual(punteggio_priorita("bassa"), 0)
        self.assertEqual(punteggio_priorita("sconosciuta"), 0)

        task = [("backup", "alta"), ("patch", "critica"), ("report", "media"), ("audit", "alta")]
        ordinati = ordina_task_per_priorita(task)
        self.assertEqual(ordinati, [("patch", "critica"), ("audit", "alta"), ("backup", "alta"), ("report", "media")])

    def test_07_riepilogo_bilancio(self):
        tx = [
            {"categoria": "stipendio", "importo": 2000.0, "tipo": "entrata"},
            {"categoria": "affitto", "importo": 800.0, "tipo": "uscita"},
            {"categoria": "spesa", "importo": 150.0, "tipo": "uscita"},
            {"categoria": "spesa", "importo": 50.0, "tipo": "uscita"},
        ]
        res = riepilogo_bilancio(tx)
        self.assertAlmostEqual(res["totale_entrate"], 2000.0)
        self.assertAlmostEqual(res["totale_uscite"], 1000.0)
        self.assertAlmostEqual(res["saldo"], 1000.0)
        self.assertEqual(res["per_categoria"]["stipendio"], 2000.0)
        self.assertEqual(res["per_categoria"]["affitto"], -800.0)
        self.assertEqual(res["per_categoria"]["spesa"], -200.0)

    def test_08_estrai_keyword(self):
        testi = [
            "Python è bello e potente",
            "Potente e semplice da imparare",
            "Scrivi codice bello"
        ]
        stop = {"e", "da", "è"}
        kw = estrai_keyword(testi, stop, minimo=5)
        self.assertEqual(kw, {"python", "bello", "potente", "semplice", "imparare", "scrivi", "codice"})

    def test_09_primo_quadrato_maggiore_di(self):
        self.assertEqual(primo_quadrato_maggiore_di([1, 2, 3, 4, 5], 10), (4, 3))
        self.assertEqual(primo_quadrato_maggiore_di([3, 4, 5], 16), (5, 2))
        self.assertIsNone(primo_quadrato_maggiore_di([1, 2, 3], 10**6))

    def test_10_raggruppa_anagrammi(self):
        parole = ["Roma", "amor", "ramo", "cane", "neca", "Mora"]
        gruppi = raggruppa_anagrammi(parole)
        chiave_ramor = tuple(sorted("amor"))
        chiave_cane = tuple(sorted("cane"))
        self.assertEqual(gruppi[chiave_ramor], ["Roma", "amor", "ramo", "Mora"])
        self.assertEqual(gruppi[chiave_cane], ["cane", "neca"])
        # Le chiavi devono essere tuple
        for k in gruppi.keys():
            self.assertIsInstance(k, tuple)


# Reporter semplice
def _run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestEserciziGiorno1)
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
