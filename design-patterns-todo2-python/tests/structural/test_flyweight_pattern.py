from structural.flyweight_pattern import IconFactory, IconFlyweight, render_map


def test_icon_factory_reuses_flyweights() -> None:
    factory = IconFactory()
    first = factory.get_icon("pin", "red")
    second = factory.get_icon("pin", "red")
    other = factory.get_icon("pin", "blue")

    assert first is second
    assert first is not other
    assert isinstance(first, IconFlyweight)


def test_render_map_composes_extrinsic_state() -> None:
    factory = IconFactory()
    result = render_map(
        factory,
        [
            ("pin", "red", (10, 20)),
            ("pin", "red", (15, 25)),
            ("house", "green", (5, 5)),
        ],
    )
    assert result == [
        "Rendering red pin at (10, 20)",
        "Rendering red pin at (15, 25)",
        "Rendering green house at (5, 5)",
    ]
