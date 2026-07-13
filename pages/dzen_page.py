from pages.base_page import BasePage


class DzenPage(BasePage):
    def is_loaded(self):
        return "dzen" in self.driver.current_url.lower() or "yandex" in self.driver.current_url.lower()
