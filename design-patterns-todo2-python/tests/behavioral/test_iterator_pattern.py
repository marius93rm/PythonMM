import pytest

from behavioral.iterator_pattern import Playlist, PlaylistIterator, build_playlist


def test_playlist_iterator_yields_tracks_in_order() -> None:
    playlist = build_playlist("Intro", "Verse", "Chorus")
    assert list(playlist) == ["Intro", "Verse", "Chorus"]


def test_iterator_raises_stop_iteration_when_finished() -> None:
    playlist = Playlist()
    playlist.add_track("Solo")

    iterator = iter(playlist)
    assert next(iterator) == "Solo"
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_isolated_from_mutations() -> None:
    playlist = build_playlist("One", "Two")
    iterator = PlaylistIterator(playlist)
    playlist.add_track("Three")

    assert list(iterator) == ["One", "Two"]
