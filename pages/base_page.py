from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from config import BASE_URL, WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def open(self):
        self.driver.get(BASE_URL)
        self.wait.until(EC.url_contains("qa-scooter.praktikum-services.ru"))

    # Element interaction methods
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_input(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    # Driver interaction methods
    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def execute_script(self, script, element=None):
        if element:
            return self.driver.execute_script(script, element)
        return self.driver.execute_script(script)

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def send_keys(self, locator, keys):
        element = self.driver.find_element(*locator)
        element.send_keys(keys)

    def press_key(self, key):
        """Press a keyboard key using the body element"""
        self.driver.find_element("tag name", "body").send_keys(key)
