"""Soluzione commentata del pattern Adapter."""

from __future__ import annotations

from abc import ABC, abstractmethod


class AudioPlayer(ABC):
    """Interfaccia moderna per la riproduzione audio."""

    @abstractmethod
    def play_sound(self, file_path: str) -> None:
        """Riproduce il file indicato."""


class LegacyAudioSystem:
    """Simula una libreria legacy con interfaccia non compatibile."""

    def playFile(self, path: str) -> None:  # noqa: N802 - simuliamo convenzione legacy
        print(f"Legacy playing {path}")


class LegacyAudioAdapter(AudioPlayer):
    """Adapter che traduce la chiamata moderna verso il sistema legacy."""

    def __init__(self, legacy_system: LegacyAudioSystem) -> None:
        self._legacy = legacy_system

    def play_sound(self, file_path: str) -> None:
        # L'adapter converte la chiamata moderna nel formato atteso dal sistema legacy.
        self._legacy.playFile(file_path)


class ModernAudioPlayer(AudioPlayer):
    """Player che utilizza un adapter per parlare con la libreria legacy."""

    def __init__(self, adapter: AudioPlayer) -> None:
        self._adapter = adapter

    def play_sound(self, file_path: str) -> None:
        # Il player potrebbe aggiungere pre-processing o logging prima di delegare.
        print(f"Modern player preparing {file_path}")
        self._adapter.play_sound(file_path)


def demo_playback(player: AudioPlayer, demo_file: str) -> None:
    """Funzione di supporto per test manuali."""
    player.play_sound(demo_file)
