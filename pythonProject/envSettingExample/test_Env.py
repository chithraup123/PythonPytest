from pytest import mark


@mark.env
def test_env_is_qa(app_config):
    assert app_config.baseUrl == 'httpsc://www.saucedemo.com/'
    assert app_config.app_port == 8088


@mark.env
def test_env_is_dev(app_config):
    assert app_config.baseUrl == 'https://www.google.com'
    assert app_config.app_port == 8080
