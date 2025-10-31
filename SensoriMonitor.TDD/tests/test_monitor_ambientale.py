"""Test guidati per MonitorAmbientale (milestone 2, 3 e 4).

Ogni test introduce una nuova funzionalità. Ricorda di completare un TODO alla
volta, far fallire il test, poi implementare il codice minimo per farlo passare.
"""

from unittest.mock import Mock

import pytest

from lettura_sensore import LetturaSensore
from monitor_ambientale import MonitorAmbientale


# TODO 2.T1: completa questo test per guidare l'implementazione dello storico.
def test_monitor_memorizza_letture_in_ordine():
    """Lo storico deve conservare le letture nell'ordine di inserimento."""
    monitor = MonitorAmbientale()

    # ARRANGE: crea due letture di prova (puoi usare direttamente LetturaSensore o finti oggetti).
    lettura1 = ...
    lettura2 = ...

    # ACT: aggiungi le letture al monitor.
    ...
    ...

    # ASSERT: verifica che tutte_le_letture ritorni l'ordine atteso.
    storico = monitor.tutte_le_letture()
    assert list(storico) == [..., ...]


# TODO 3.T1: guida la logica di soglia con un test esplicito.
def test_monitor_rileva_allarme_fuori_soglia():
    """Una lettura fuori soglia deve far scattare l'allarme."""
    monitor = MonitorAmbientale()
    lettura_fuori_soglia = ...  # scegli valori che superino le soglie previste dai test

    # ACT + ASSERT: il metodo pubblico deve segnalare l'allarme.
    assert monitor.is_allarme(lettura_fuori_soglia) is ...

    # Puoi aggiungere un caso positivo (nessun allarme) per completare il ragionamento.
    lettura_normale = ...
    assert monitor.is_allarme(lettura_normale) is ...


# TODO 4.T1: integra un notificatore mock e verifica che venga chiamato quando serve.
def test_monitor_notifica_allarme_con_mock():
    """Quando l'allarme scatta, il monitor deve notificare l'esterno."""
    notificatore_mock = Mock()
    monitor = MonitorAmbientale(notificatore=notificatore_mock)

    lettura_pericolosa = ...

    # ACT: aggiungi la lettura pericolosa; il metodo dovrebbe gestire la notifica.
    monitor.aggiungi_lettura(lettura_pericolosa)

    # ASSERT: il mock deve essere stato chiamato almeno una volta con un messaggio.
    notificatore_mock.manda_alert.assert_called_with(...)
