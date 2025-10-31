"""Pattern Factory Method
=========================
Cos'è il pattern:
    Il Factory Method delega alle sottoclassi la responsabilità di creare oggetti specifici.
Obiettivo didattico:
    Comprendere come isolare la logica di creazione e rendere estensibile il sistema.
Scenario proposto:
    Un sistema di notifiche deve inviare messaggi via email o SMS in base a un tipo scelto a runtime.
Cosa deve fare lo studente:
    Definire l'interfaccia comune, implementare le notifiche concrete e completare la factory.
Passi TODO:
    1. Completare l'interfaccia `Notification` con il metodo `send`.
    2. Implementare le classi concrete `EmailNotification` e `SmsNotification`.
    3. Completare `NotificationFactory.create_notification` con la logica di selezione e gestione errori.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Notification(ABC):
    """Interfaccia comune per ogni canale di notifica."""

    # TODO: dichiarare il metodo astratto send(message: str) -> None


class EmailNotification(Notification):
    """Invia una notifica via email."""

    # TODO: implementare il metodo send
    ...


class SmsNotification(Notification):
    """Invia una notifica via SMS."""

    # TODO: implementare il metodo send
    ...


class NotificationFactory:
    """Factory che restituisce un oggetto Notification a partire da una stringa."""

    def create_notification(self, channel: str) -> Notification:
        """Restituisce la notifica appropriata in base al canale richiesto."""
        normalized = channel.strip().lower()
        # TODO: restituire EmailNotification per "email"
        # TODO: restituire SmsNotification per "sms"
        # TODO: sollevare ValueError per canali non supportati
        raise NotImplementedError("Selezione del canale non ancora implementata")


def demo(factory: NotificationFactory) -> None:
    """Esempio di utilizzo della factory.

    Questo metodo può essere usato nei test manuali: crea una notifica tramite la factory
    e invoca il metodo `send`. Inserisci eventualmente delle stampe personalizzate quando
    avrai completato i TODO.
    """

    # TODO: utilizzare la factory per creare una notifica fittizia e chiamare send()
    raise NotImplementedError("Scrivere una piccola demo una volta completata la factory")
