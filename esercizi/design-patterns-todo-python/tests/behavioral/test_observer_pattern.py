import pytest

from behavioral.observer_pattern import DisplayObserver, WeatherStation


def test_observers_receive_updates_from_station() -> None:
    station = WeatherStation()
    display = DisplayObserver(name="Outdoor")
    station.attach(display)

    station.update_measurements(temperature=21.5, humidity=0.45)

    assert display.last_temperature == 21.5
    assert display.last_humidity == 0.45


def test_detach_prevents_further_notifications() -> None:
    station = WeatherStation()
    display = DisplayObserver(name="Indoor")
    station.attach(display)
    station.update_measurements(20.0, 0.40)

    station.detach(display)
    station.update_measurements(25.0, 0.30)

    assert display.last_temperature == 20.0
    assert display.last_humidity == 0.40


def test_attach_requires_unique_instances() -> None:
    station = WeatherStation()
    display = DisplayObserver(name="Desk")
    station.attach(display)

    with pytest.raises(ValueError):
        station.attach(display)
