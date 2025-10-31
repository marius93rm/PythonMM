from creational.singleton_pattern import AppConfig, get_app_config


def test_singleton_returns_same_instance() -> None:
    config_a = AppConfig("MyApp", debug=True)
    config_b = AppConfig("Other", debug=False)

    assert config_a is config_b
    assert config_b.app_name == "MyApp"
    assert config_b.debug is True


def test_get_app_config_returns_initialized_instance() -> None:
    config = get_app_config()
    other = get_app_config()
    assert config is other
    assert isinstance(config, AppConfig)
