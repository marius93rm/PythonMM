"""Test risolti per la milestone 1."""

from datetime import datetime

import pytest

from lettura_sensore import LetturaSensore


def test_crea_lettura_sensore():
    """Verifica che la lettura memorizzi i dati in sola lettura."""
    temperatura = 23.5
    umidita = 45.0
    timestamp = datetime.now()

    lettura = LetturaSensore(temperatura, umidita, timestamp)

    assert lettura.temperatura == temperatura
    assert lettura.umidita == umidita
    assert lettura.timestamp == timestamp

    with pytest.raises(AttributeError):
        lettura.temperatura = 99.0
