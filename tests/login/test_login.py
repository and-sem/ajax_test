import logging
import pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from framework.login_page import LoginPage


@pytest.mark.parametrize(
    'email, password, required_element',
    [
        ('', '', LoginPage.FAILED_LOGIN_MESSAGE),
        ('qa.ajax.app.automation@gmail.com', '', LoginPage.FAILED_LOGIN_MESSAGE),
        ('qa.ajax.app.automation@gmail.com', 'wrong_password', LoginPage.FAILED_LOGIN_MESSAGE),
        ('', 'qa_automation_password', LoginPage.FAILED_LOGIN_MESSAGE),
        ('wrong@email.com', 'qa_automation_password', LoginPage.FAILED_LOGIN_MESSAGE),
        ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', LoginPage.NOTIFICATIONS_POPUP),
    ],
    ids=[
        'no credentials',
        'no password',
        'wrong password',
        'no email',
        'wrong email',
        'correct credentials',
    ]
)
def test_user_login(user_login_fixture, email, password, required_element):
    logging.info(f'Authorization attempt with credentials: email="{email}", password="{password}"')
    user_login_fixture.wait_email_input().send_keys(email)
    user_login_fixture.wait_password_input().send_keys(password)
    user_login_fixture.tap_log_in()
    logging.info('"Log in" button tapped')

    assert user_login_fixture.wait_element((By.ID, required_element)), 'No required element'
    # текст може залежати від локалізації пристрою
    logging.info('Test passed')


def test_side_bar(welcome_page):
    # якщо з'явиться попередження про блокування сповіщень, закрити його:
    try:
        welcome_page.remove_popup()
        logging.info('Notifications pop-up removed')
    except TimeoutException:
        logging.info('No pop-up')

    welcome_page.tap_sidebar()
    logging.info('Sidebar tapped')

    sidebar_elements_displayed = welcome_page.check_sidebar()
    elements_displayed = sidebar_elements_displayed.count(True)
    logging.info(f'{elements_displayed} sidebar element{"s are" if elements_displayed > 1 else " is"} displayed')

    assert all(sidebar_elements_displayed), 'Sidebar element(s) not found'
    logging.info('Test passed')
