import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.set_preference("dom.webdriver.enabled", False)
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    try:
        yield driver
    finally:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="final_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
        driver.quit()
