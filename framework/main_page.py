from selenium.webdriver.common.by import By

from .page import Page


class MainPage(Page):
    LOGIN_BUTTON = (By.ID, "com.ajaxsystems:id/login")

    def tap_login(self):
        self.find_element(self.LOGIN_BUTTON).click()
