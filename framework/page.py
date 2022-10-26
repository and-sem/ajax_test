from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def wait_element(self, locator: tuple, timeout: int = 7):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def is_displayed(self, locator):
        return self.wait_element(locator).is_displayed()
