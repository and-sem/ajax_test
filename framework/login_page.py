from selenium.webdriver.common.by import By

from .page import Page


class LoginPage(Page):
    EMAIL_INPUT = (By.ID, "com.ajaxsystems:id/login")
    PASSWORD_INPUT = (By.ID, "com.ajaxsystems:id/password")
    LOG_IN_BUTTON = (By.ID, "com.ajaxsystems:id/next")

    FAILED_LOGIN_MESSAGE = 'com.ajaxsystems:id/snackbar_text'  # з'являється при невдалій авторизації
    NOTIFICATIONS_POPUP = 'com.ajaxsystems:id/cancel_button'  # з'являється після авторизації

    def wait_email_input(self):
        return self.wait_element(self.EMAIL_INPUT).clear()

    def wait_password_input(self):
        return self.wait_element(self.PASSWORD_INPUT).clear()

    def tap_log_in(self):
        self.find_element(self.LOG_IN_BUTTON).click()
