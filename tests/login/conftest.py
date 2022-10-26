import logging

import pytest

from framework.login_page import LoginPage
from framework.main_page import MainPage
from framework.welcome_page import WelcomePage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    MainPage(driver).tap_login()
    logging.info('Authorization screen is active')
    yield LoginPage(driver)


@pytest.fixture
def welcome_page(driver):
    yield WelcomePage(driver)
