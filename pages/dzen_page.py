from pages.base_page import BasePage


class DzenPage(BasePage):
    def is_loaded(self):
        current_url = self.get_current_url().lower()
        return "dzen" in current_url or "yandex" in current_url
