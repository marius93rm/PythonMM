import pytest

from structural.adapter_pattern import (
    LegacyAudioAdapter,
    LegacyAudioSystem,
    ModernAudioPlayer,
    demo_playback,
)


def test_adapter_invokes_legacy_system(capsys: pytest.CaptureFixture[str]) -> None:
    legacy = LegacyAudioSystem()
    adapter = LegacyAudioAdapter(legacy)
    adapter.play_sound("song.mp3")
    captured = capsys.readouterr().out.strip()
    assert captured == "Legacy playing song.mp3"


def test_modern_player_delegates_to_adapter(capsys: pytest.CaptureFixture[str]) -> None:
    player = ModernAudioPlayer(LegacyAudioAdapter(LegacyAudioSystem()))
    player.play_sound("track.wav")
    assert capsys.readouterr().out.strip() == "Legacy playing track.wav"


def test_demo_playback_runs_without_errors(capsys: pytest.CaptureFixture[str]) -> None:
    player = ModernAudioPlayer(LegacyAudioAdapter(LegacyAudioSystem()))
    demo_playback(player, "demo.ogg")
    assert "Legacy playing demo.ogg" in capsys.readouterr().out
