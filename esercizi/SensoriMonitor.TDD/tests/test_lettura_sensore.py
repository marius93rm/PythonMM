"""Test per la milestone 1: modellazione di una singola lettura di sensore.

Ricorda: prima scriviamo (o completiamo) il test, lo eseguiamo e osserviamo il
fallimento (RED). Solo dopo passiamo a implementare il codice minimo in
`src/lettura_sensore.py` per ottenere il GREEN.
"""

from datetime import datetime

import pytest

from lettura_sensore import LetturaSensore


# TODO 1.T1: completa questo test seguendo i commenti.
def test_crea_lettura_sensore():
    """Verifica che la lettura memorizzi i dati in sola lettura."""
    # ARRANGE: prepara dati di esempio leggibili.
    temperatura = ...  # scegli un float
    umidita = ...  # scegli un altro float
    timestamp = ...  # puoi usare datetime.now() oppure una stringa ISO

    # ACT: istanzia la classe. Questo dovrebbe fallire finché non implementi il TODO 1.1.
    lettura = ...  # LetturaSensore(temperatura, umidita, timestamp)

    # ASSERT: verifica che i valori siano memorizzati correttamente.
    assert lettura.temperatura == ...
    assert lettura.umidita == ...
    assert lettura.timestamp == ...

    # Extra: verifica che gli attributi siano in sola lettura.
    with pytest.raises(AttributeError):
        # Prova a modificare un attributo esposto: l'implementazione dovrebbe impedirlo.
        lettura.temperatura = ...
