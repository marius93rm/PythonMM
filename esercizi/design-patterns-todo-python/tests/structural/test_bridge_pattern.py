from structural.bridge_pattern import (
    AdvancedRemote,
    BasicRemote,
    Radio,
    RemoteControl,
    Television,
)


def test_toggle_power_switches_device_state() -> None:
    tv = Television()
    remote: RemoteControl = BasicRemote(tv)

    remote.toggle_power()
    assert tv.is_on() is True

    remote.toggle_power()
    assert tv.is_on() is False


def test_volume_controls_delegate_to_device() -> None:
    radio = Radio()
    remote = BasicRemote(radio)

    remote.toggle_power()
    remote.volume_up()
    remote.volume_up()
    assert radio.get_volume() == 70

    remote.volume_down()
    assert radio.get_volume() == 60


def test_advanced_remote_mute_sets_volume_zero() -> None:
    tv = Television()
    remote = AdvancedRemote(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.mute()
    assert tv.get_volume() == 0
