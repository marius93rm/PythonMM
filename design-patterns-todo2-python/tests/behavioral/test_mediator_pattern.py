from behavioral.mediator_pattern import ChatRoomMediator, User, start_demo_chat


def test_user_auto_registers_and_receives_messages() -> None:
    mediator = ChatRoomMediator()
    alice = User("Alice", mediator)
    bob = User("Bob", mediator)

    alice.send("Hello!")

    assert ("Alice", "Hello!") in bob.inbox
    assert bob not in mediator._users.values() or mediator._users["Bob"] is bob


def test_start_demo_chat_populates_users() -> None:
    mediator = start_demo_chat(["Anna", "Luca", "Mia"])
    assert sorted(mediator._users.keys()) == ["Anna", "Luca", "Mia"]

    sender = mediator._users["Anna"]
    sender.send("Ciao a tutti")

    for name, user in mediator._users.items():
        if name != "Anna":
            assert ("Anna", "Ciao a tutti") in user.inbox
