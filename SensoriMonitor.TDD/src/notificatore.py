"""Definizione di un notificatore di allarmi generico.

In un'applicazione reale questo oggetto potrebbe inviare email, messaggi Slack
oppure scrivere su un sistema di logging centralizzato. Nel nostro esercizio lo
useremo soprattutto come dipendenza da mockare nei test.
"""

from __future__ import annotations


class NotificatoreAllarmi:
    """Interfaccia minimale per l'invio di notifiche di allarme."""

    # TODO 4.1: personalizza questo metodo se vuoi simulare comportamenti reali.
    #           Nei test useremo `unittest.mock` per verificare che venga chiamato.
    def manda_alert(self, messaggio: str) -> None:  # pragma: no cover - da implementare in produzione
        """Invia un messaggio di allarme verso un canale esterno."""
        pass
