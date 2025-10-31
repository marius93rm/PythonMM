from structural.proxy_pattern import ProxyImage, RealImage, load_gallery


def test_real_image_display_returns_message() -> None:
    image = RealImage("photo.png")
    assert image.loaded is True
    assert image.display() == "Displaying photo.png"


def test_proxy_creates_real_image_lazily() -> None:
    proxy = ProxyImage("diagram.svg")
    assert proxy._real_image is None
    first = proxy.display()
    second = proxy.display()
    assert first == "Displaying diagram.svg"
    assert second == "Displaying diagram.svg"
    assert proxy._real_image is not None


def test_load_gallery_invokes_display_on_each_image() -> None:
    images = [ProxyImage("a.jpg"), ProxyImage("b.jpg")]
    results = load_gallery(images)
    assert results == ["Displaying a.jpg", "Displaying b.jpg"]
