import pytest

from creational.abstract_factory_pattern import (
    DarkUIFactory,
    LightUIFactory,
    UIComponentFactory,
    demo_render,
)


@pytest.mark.parametrize(
    "factory,expected",
    [
        (LightUIFactory(), ["Rendering light button", "Rendering light checkbox"]),
        (DarkUIFactory(), ["Rendering dark button", "Rendering dark checkbox"]),
    ],
)
def test_demo_render_produces_theme_consistent_components(
    factory: UIComponentFactory, expected: list[str]
) -> None:
    assert demo_render(factory) == expected
