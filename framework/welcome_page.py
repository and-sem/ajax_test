from selenium.webdriver.common.by import By

from .page import Page


class WelcomePage(Page):
    REMOVE_POPUP = (By.ID, "com.ajaxsystems:id/cancel_button")
    SIDEBAR = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/menuDrawer']")

    ADD_HUB = (By.ID, "com.ajaxsystems:id/addHub")
    APP_SETTINGS = (By.ID, "com.ajaxsystems:id/settings")
    HELP = (By.ID, "com.ajaxsystems:id/help")
    REPORT_A_PROBLEM = (By.ID, "com.ajaxsystems:id/logs")
    VIDEO_SURVEILLANCE = (By.ID, "com.ajaxsystems:id/camera")

    def remove_popup(self):
        self.wait_element(self.REMOVE_POPUP).click()

    def tap_sidebar(self):
        self.wait_element(self.SIDEBAR).click()

    def check_sidebar(self):
        return (
            self.is_displayed(self.ADD_HUB),
            self.is_displayed(self.APP_SETTINGS),
            self.is_displayed(self.HELP),
            self.is_displayed(self.REPORT_A_PROBLEM),
            self.is_displayed(self.VIDEO_SURVEILLANCE),
        )
