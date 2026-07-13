import allure
import pytest

from pages.main_page import MainPage


@allure.feature("FAQ")
class TestFAQ:
    @pytest.mark.parametrize(
        "question_index, expected_text",
        [
            (0, "400"),
            (1, "один самокат"),
            (2, "в течение дня"),
            (3, "завтрашнего"),
            (4, "срочное"),
            (5, "полной зарядкой"),
            (6, "самокат не привезли"),
            (7, "Москве"),
        ],
    )
    def test_faq_item_shows_expected_answer(self, driver, question_index, expected_text):
        main_page = MainPage(driver)
        main_page.open()

        with allure.step(f"Открываю ответ на вопрос №{question_index + 1}"):
            main_page.expand_faq_item(question_index)

        with allure.step("Проверяю, что появился текст ответа"):
            answer_text = main_page.get_faq_answer_text(question_index)
            assert expected_text.lower() in answer_text.lower()
