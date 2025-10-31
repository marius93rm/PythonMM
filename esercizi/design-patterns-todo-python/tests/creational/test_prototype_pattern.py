from creational.prototype_pattern import Circle, Shape, clone_and_shift


def test_circle_clone_creates_distinct_instance() -> None:
    original = Circle("red", 3.5)
    clone = original.clone()

    assert isinstance(clone, Circle)
    assert clone is not original
    assert clone.color == original.color
    assert clone.radius == original.radius


def test_clone_and_shift_updates_color_without_affecting_original() -> None:
    original = Circle("blue", 2.0)
    mutated = clone_and_shift(original, color="green")

    assert isinstance(mutated, Shape)
    assert mutated.color == "green"
    assert original.color == "blue"
