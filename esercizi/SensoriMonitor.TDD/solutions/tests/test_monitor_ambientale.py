"""Test risolti per MonitorAmbientale."""

from unittest.mock import Mock

from lettura_sensore import LetturaSensore
from monitor_ambientale import MonitorAmbientale


def test_monitor_memorizza_letture_in_ordine():
    monitor = MonitorAmbientale()

    lettura1 = LetturaSensore(22.5, 40.0, "2024-01-01T10:00:00")
    lettura2 = LetturaSensore(23.0, 42.0, "2024-01-01T11:00:00")

    monitor.aggiungi_lettura(lettura1)
    monitor.aggiungi_lettura(lettura2)

    storico = monitor.tutte_le_letture()
    assert list(storico) == [lettura1, lettura2]


def test_monitor_rileva_allarme_fuori_soglia():
    monitor = MonitorAmbientale()

    lettura_fuori_soglia = LetturaSensore(55.0, 25.0, "2024-01-01T12:00:00")
    assert monitor.is_allarme(lettura_fuori_soglia) is True

    lettura_normale = LetturaSensore(25.0, 45.0, "2024-01-01T13:00:00")
    assert monitor.is_allarme(lettura_normale) is False


def test_monitor_notifica_allarme_con_mock():
    notificatore_mock = Mock()
    monitor = MonitorAmbientale(notificatore=notificatore_mock)

    lettura_pericolosa = LetturaSensore(60.0, 15.0, "2024-01-01T14:00:00")

    monitor.aggiungi_lettura(lettura_pericolosa)

    notificatore_mock.manda_alert.assert_called_once_with(
        "Allarme rilevato: temperatura=60.0, umidita=15.0"
    )
