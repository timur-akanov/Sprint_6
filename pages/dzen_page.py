import allure

from pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step("Check if Dzen/Yandex page is loaded")
    def is_loaded(self):
        current_url = self.get_current_url().lower()
        return "dzen" in current_url or "yandex" in current_url
