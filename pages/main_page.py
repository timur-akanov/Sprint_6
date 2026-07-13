from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    FAQ_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")
    FAQ_ANSWER_PANELS = (By.CSS_SELECTOR, ".accordion__panel")
    ORDER_BUTTON_HEADER = (By.XPATH, "(//button[contains(., 'Заказать')])[1]")
    ORDER_BUTTON_FOOTER = (By.XPATH, "(//button[contains(., 'Заказать')])[2]")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[href='/']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[href*='yandex']")
    HOME_PAGE_BUTTONS = (By.XPATH, "//button[contains(., 'Заказать')]")

    def open(self):
        super().open()
        self.remove_cookie_banner()

    def remove_cookie_banner(self):
        self.driver.execute_script("""
        const overlay = document.querySelector('[class*="CookieConsent"]');
        if (overlay) overlay.remove();
        """)

    def expand_faq_item(self, index):
        buttons = self.driver.find_elements(*self.FAQ_BUTTONS)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[index])
        self.driver.execute_script("arguments[0].click();", buttons[index])

    def get_faq_answer_text(self, index):
        panels = self.driver.find_elements(*self.FAQ_ANSWER_PANELS)
        return self.driver.execute_script("return arguments[0].textContent;", panels[index]).strip()

    def click_order_button(self, entry_point):
        self.remove_cookie_banner()
        locator = self.ORDER_BUTTON_HEADER if entry_point == "header" else self.ORDER_BUTTON_FOOTER
        self.click(locator)

    def click_scooter_logo(self):
        element = self.driver.find_element(*self.SCOOTER_LOGO)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_yandex_logo(self):
        element = self.driver.find_element(*self.YANDEX_LOGO)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda driver: "dzen" in driver.current_url.lower() or "yandex" in driver.current_url.lower())

    def is_home_page_open(self):
        return self.driver.current_url.startswith(self.BASE_URL) and self.driver.find_element(*self.HOME_PAGE_BUTTONS).is_displayed()
