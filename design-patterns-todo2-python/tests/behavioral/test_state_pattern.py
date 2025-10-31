import pytest

from behavioral.state_pattern import (
    DeliveredOrderState,
    NewOrderState,
    Order,
    ShippedOrderState,
    create_order,
)


def test_order_initializes_in_new_state() -> None:
    order = create_order()
    assert isinstance(order.state, NewOrderState)


def test_order_transitions_through_states() -> None:
    order = Order()
    order.next_step()
    assert isinstance(order.state, ShippedOrderState)

    order.next_step()
    assert isinstance(order.state, DeliveredOrderState)

    order.next_step()
    assert isinstance(order.state, DeliveredOrderState)


def test_set_state_accepts_custom_state() -> None:
    order = Order()

    class CustomState(NewOrderState):
        def next_step(self, order: Order) -> None:
            order.set_state(DeliveredOrderState())

    custom = CustomState()
    order.set_state(custom)
    assert order.state is custom
    order.next_step()
    assert isinstance(order.state, DeliveredOrderState)
