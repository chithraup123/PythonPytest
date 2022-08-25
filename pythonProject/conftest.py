from pytest import fixture

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import Config


@fixture(scope='function')
# for each test function one separate browser will get used if scope is function
def edge_driver():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    yield driver

    print("Im tearing down this browser")


# @fixture(scope='session')
# for entire testcases only one browser gets used if scope is session
# def edge_driver():
#     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     return driver

########################################################################
# helps to add custom option and fixture helps to return the stored option

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     # default="dev",
                     help="Environment to run tests against"
                     )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
