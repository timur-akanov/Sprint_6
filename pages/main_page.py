import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config import BASE_URL


class MainPage(BasePage):
    FAQ_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")
    FAQ_ANSWER_PANELS = (By.CSS_SELECTOR, ".accordion__panel")
    ORDER_BUTTON_HEADER = (By.XPATH, "(//button[contains(., 'Заказать')])[1]")
    ORDER_BUTTON_FOOTER = (By.XPATH, "(//button[contains(., 'Заказать')])[2]")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[href*='yandex']")
    HOME_PAGE_BUTTONS = (By.XPATH, "//button[contains(., 'Заказать')]")

    @allure.step("Open main page and remove cookie banner")
    def open(self):
        super().open()
        self.remove_cookie_banner()

    @allure.step("Remove cookie consent banner")
    def remove_cookie_banner(self):
        self.execute_script("""
        const overlay = document.querySelector('[class*="CookieConsent"]');
        if (overlay) overlay.remove();
        """)

    @allure.step("Expand FAQ item at index {index}")
    def expand_faq_item(self, index):
        buttons = self.find_elements(self.FAQ_BUTTONS)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[index])
        self.execute_script("arguments[0].click();", buttons[index])

    @allure.step("Get FAQ answer text at index {index}")
    def get_faq_answer_text(self, index):
        panels = self.find_elements(self.FAQ_ANSWER_PANELS)
        return self.execute_script("return arguments[0].textContent;", panels[index]).strip()

    @allure.step("Click order button from {entry_point}")
    def click_order_button(self, entry_point):
        self.remove_cookie_banner()
        locator = self.ORDER_BUTTON_HEADER if entry_point == "header" else self.ORDER_BUTTON_FOOTER
        self.click(locator)

    @allure.step("Click Scooter logo")
    def click_scooter_logo(self):
        element = self.find_element(self.SCOOTER_LOGO)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Click Yandex logo and switch to new window")
    def click_yandex_logo(self):
        element = self.find_element(self.YANDEX_LOGO)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.execute_script("arguments[0].click();", element)
        self.wait.until(lambda driver: len(self.get_window_handles()) > 1)
        self.switch_to_window(self.get_window_handles()[-1])
        self.wait.until(lambda driver: "dzen" in self.get_current_url().lower() or "yandex" in self.get_current_url().lower())

    @allure.step("Verify home page is open")
    def is_home_page_open(self):
        return self.get_current_url().startswith(BASE_URL) and self.find_element(self.HOME_PAGE_BUTTONS).is_displayed()
