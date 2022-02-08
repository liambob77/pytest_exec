# test_spam.py
# from urllib import request
from matplotlib.pyplot import title
import pytest
import _pytest
# from .conftest import option
from pprint import pprint
import allure

import os

def the_name():
    return os.environ.get('TEST_NAME')

# pprint(option)
# print(dir(_pytest.config))

config = None
name = the_name()

# @pytest.fixture(autouse=True)
# def inject_config1(request):
#     global config
#     config = request.config


@allure.suite(name)
class Tests():
    _config = "abc"

    @pytest.fixture(autouse=True)
    def inject_config(self, request):
        self._config = request.config

    def test_selenium(self, test_data):
        test_data.add_a()
        allure.dynamic.title(self._config.option.setup)
        assert 1
        # print(dir(self))

    def test_selenium2(self, test_data):
        test_data.add_a()
        allure.dynamic.title(self._config.option.setup)
        assert 1
        # print(dir(self))

def test_lalala():
    allure.epic("abc", Tests)
