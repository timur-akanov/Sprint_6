import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage


@allure.feature("Заказ самоката")
class TestOrderFlow:
    @pytest.mark.parametrize(
        "entry_point, user_data",
        [
            ("header", {"name": "Иван", "last_name": "Иванов", "address": "ул. Ленина, 10", "metro": "Черкизовская", "phone": "+79991234567"}),
            ("footer", {"name": "Мария", "last_name": "Петрова", "address": "пр. Мира, 25", "metro": "Сокольники", "phone": "+79997654321"}),
        ],
    )
    def test_order_flow_from_different_entry_points(self, driver, entry_point, user_data):
        main_page = MainPage(driver)
        main_page.open()

        with allure.step(f"Нажимаю кнопку Заказать через {entry_point}"):
            main_page.click_order_button(entry_point)

        order_page = OrderPage(driver)

        with allure.step("Заполняю первую форму заказа"):
            order_page.fill_customer_form(
                name=user_data["name"],
                last_name=user_data["last_name"],
                address=user_data["address"],
                metro=user_data["metro"],
                phone=user_data["phone"],
            )
            order_page.continue_to_next_step()

        with allure.step("Заполняю вторую форму заказа"):
            order_page.fill_delivery_details()
            order_page.confirm_order()

        with allure.step("Проверяю всплывающее окно об успешном заказе"):
            assert order_page.is_success_message_displayed()

        with allure.step("Проверяю переход на главную страницу по логотипу Самоката"):
            main_page.click_scooter_logo()
            assert main_page.is_home_page_open()

        with allure.step("Проверяю переход на Дзен по логотипу Яндекса"):
            main_page.click_yandex_logo()
            dzen_page = DzenPage(driver)
            assert dzen_page.is_loaded()
