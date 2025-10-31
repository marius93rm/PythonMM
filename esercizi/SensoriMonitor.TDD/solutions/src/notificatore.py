"""Implementazione di esempio per NotificatoreAllarmi."""

from __future__ import annotations


class NotificatoreAllarmi:
    """Notificatore minimale: stampa il messaggio su standard output."""

    def manda_alert(self, messaggio: str) -> None:
        print(f"[ALLARME] {messaggio}")
