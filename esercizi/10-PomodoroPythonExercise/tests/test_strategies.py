import pytest
from pomodoro.sessions import Classic25_5, Deep50_10, Custom

def test_classic_and_deep():
    assert Classic25_5().get_durations() == (25*60, 5*60)
    assert Deep50_10().get_durations() == (50*60, 10*60)

def test_custom_validation():
    with pytest.raises(Exception):
        # finché non implementi la validazione, questo potrebbe non sollevare
        # quindi fallirà: implementa e lancia ValueError se <= 0
        Custom(0, 5)
