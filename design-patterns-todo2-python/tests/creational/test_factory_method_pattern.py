import pytest

from creational.factory_method_pattern import NotificationFactory, demo


def test_factory_creates_notifications_by_channel() -> None:
    factory = NotificationFactory()
    email = factory.create_notification("email")
    sms = factory.create_notification("sms")

    assert email.send("Welcome") == "Email notification: Welcome"
    assert sms.send("Code: 1234") == "SMS notification: Code: 1234"


@pytest.mark.parametrize("channel", ["push", "", "unknown"])
def test_factory_rejects_unknown_channels(channel: str) -> None:
    factory = NotificationFactory()
    with pytest.raises(ValueError):
        factory.create_notification(channel)


def test_demo_runs_example_notification(capsys: pytest.CaptureFixture[str]) -> None:
    factory = NotificationFactory()
    demo(factory)
    output = capsys.readouterr().out.strip()
    assert "Email notification:" in output or "SMS notification:" in output
