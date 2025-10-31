"""Pattern State
================
Cos'è il pattern:
    Lo State incapsula comportamenti dipendenti dallo stato evitando lunghi blocchi condizionali.
Obiettivo didattico:
    Modellare gli stati di un ordine e le transizioni tra di essi.
Scenario proposto:
    Un oggetto `Order` passa da New a Shipped a Delivered, con comportamento diverso per `next_step()`.
Cosa deve fare lo studente:
    Definire gli stati concreti e far sì che l'ordine deleghi loro le transizioni.
Passi TODO:
    1. Creare l'interfaccia `OrderState` con il metodo `next_step(order)`.
    2. Implementare gli stati concreti che impostano il prossimo stato.
    3. Gestire la logica in `Order` per inizializzare e delegare.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class OrderState(ABC):
    """Interfaccia per gli stati dell'ordine."""

    # TODO: dichiarare metodo astratto next_step(order: "Order") -> None


class NewOrderState(OrderState):
    """Stato iniziale dell'ordine."""

    def next_step(self, order: "Order") -> None:
        # TODO: impostare il prossimo stato e magari registrare un messaggio
        raise NotImplementedError("Implementare transizione da New a Shipped")


class ShippedOrderState(OrderState):
    """Stato in cui l'ordine è stato spedito."""

    def next_step(self, order: "Order") -> None:
        # TODO: impostare il prossimo stato e gestire eventuale logistica
        raise NotImplementedError("Implementare transizione da Shipped a Delivered")


class DeliveredOrderState(OrderState):
    """Stato finale dell'ordine."""

    def next_step(self, order: "Order") -> None:
        # TODO: decidere cosa accade quando l'ordine è già consegnato
        raise NotImplementedError("Gestire stato finale")


class Order:
    """Contesto che mantiene lo stato corrente."""

    def __init__(self) -> None:
        # TODO: inizializzare lo stato a NewOrderState
        raise NotImplementedError("Inizializzare l'ordine con lo stato corretto")

    def next_step(self) -> None:
        # TODO: delegare la logica allo stato corrente
        raise NotImplementedError("Delegare la transizione allo stato")

    @property
    def state(self) -> OrderState:
        return self._state

    def set_state(self, state: OrderState) -> None:
        # TODO: aggiornare lo stato corrente
        raise NotImplementedError("Aggiornare lo stato dell'ordine")


def create_order() -> Order:
    """Utility per ottenere un ordine nello stato iniziale."""
    # TODO: restituire un'istanza di Order pronta all'uso
    raise NotImplementedError("Creare un ordine di esempio")
