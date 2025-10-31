from structural.facade_pattern import VideoConverterFacade


def test_facade_runs_full_conversion_pipeline() -> None:
    facade = VideoConverterFacade()
    result = facade.convert("video.mov", "output.mp4", format="mp4")
    assert result == "Saved encoded(video.mov->mp4) to output.mp4"


def test_facade_can_be_reused_for_multiple_conversions() -> None:
    facade = VideoConverterFacade()
    first = facade.convert("clip.avi", "clip.mp4", format="mp4")
    second = facade.convert("clip.avi", "clip.webm", format="webm")
    assert first.endswith("clip.mp4")
    assert second.endswith("clip.webm")
