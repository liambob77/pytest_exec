import os
import pytest


option = None

def pytest_generate_tests(metafunc):
    os.environ['TEST_NAME'] = 'My super test name| Python version'

def pytest_addoption(parser):
    parser.addoption('--spam', action='store', default="type1")

def pytest_addoption(parser):
    os.environ['TEST_NAME'] = 'My super test name| Python version'
    parser.addoption("--setup", "--sC=", action="store", dest="setup", default="type1", help="setup.")

def pytest_configure(config):
    global option
    option = config.option
    print(f"config.option.setup:  {config.option.setup}")


def singleton(cls):
    _instance = {}

    def inner(*arg, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*arg, **kargs)
        return _instance[cls]
    return inner

@singleton
class A_helper:
    def __init__(self, fixture):
        self.fixture = fixture
        self.a = 10

    def add_a(self):
        self.a += 1

@pytest.fixture
def test_data(request):
    a = A_helper(request)
    a.add_a()
    yield a