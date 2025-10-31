"""Soluzione commentata del pattern State."""

from __future__ import annotations

from abc import ABC, abstractmethod


class OrderState(ABC):
    """Interfaccia per gli stati dell'ordine."""

    @abstractmethod
    def next_step(self, order: "Order") -> None:
        """Esegue la transizione allo stato successivo."""


class NewOrderState(OrderState):
    """Stato iniziale dell'ordine."""

    def next_step(self, order: "Order") -> None:
        print("Ordine preparato, passa a SHIPPED")
        order.set_state(ShippedOrderState())


class ShippedOrderState(OrderState):
    """Stato in cui l'ordine è stato spedito."""

    def next_step(self, order: "Order") -> None:
        print("Ordine consegnato al corriere, passa a DELIVERED")
        order.set_state(DeliveredOrderState())


class DeliveredOrderState(OrderState):
    """Stato finale dell'ordine."""

    def next_step(self, order: "Order") -> None:
        print("Ordine già consegnato: nessuna ulteriore transizione.")


class Order:
    """Contesto che mantiene lo stato corrente."""

    def __init__(self) -> None:
        self._state: OrderState = NewOrderState()

    def next_step(self) -> None:
        self._state.next_step(self)

    @property
    def state(self) -> OrderState:
        return self._state

    def set_state(self, state: OrderState) -> None:
        self._state = state


def create_order() -> Order:
    """Utility per ottenere un ordine nello stato iniziale."""
    return Order()
