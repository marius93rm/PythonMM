"""Soluzione commentata del pattern Iterator."""

from __future__ import annotations

from collections.abc import Iterator
from typing import List


class Playlist:
    """Collezione di tracce audio."""

    def __init__(self) -> None:
        self._tracks: List[str] = []

    def add_track(self, track: str) -> None:
        self._tracks.append(track)

    def __iter__(self) -> "PlaylistIterator":
        return PlaylistIterator(self)

    def _get_tracks(self) -> List[str]:
        """Restituisce una copia delle tracce per evitare modifiche esterne."""
        return list(self._tracks)


class PlaylistIterator(Iterator[str]):
    """Iteratore personalizzato per Playlist."""

    def __init__(self, playlist: Playlist) -> None:
        self._tracks = playlist._get_tracks()
        self._index = 0

    def __iter__(self) -> "PlaylistIterator":
        return self

    def __next__(self) -> str:
        if self._index >= len(self._tracks):
            raise StopIteration
        track = self._tracks[self._index]
        self._index += 1
        return track


def build_playlist(*tracks: str) -> Playlist:
    """Utility per popolare rapidamente una playlist."""
    playlist = Playlist()
    for track in tracks:
        playlist.add_track(track)
    return playlist
