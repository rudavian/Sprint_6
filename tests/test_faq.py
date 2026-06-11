import allure
import pytest

from data.faq_data import FAQ_DATA
from pages.main_page import MainPage


class TestFAQ:
    @allure.feature("FAQ")
    @allure.story("Вопросы о важном")
    @allure.title("Проверка текста ответа в разделе FAQ")
    @pytest.mark.parametrize("index, expected_text", FAQ_DATA)
    def test_faq_answer_text_is_displayed(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies_if_present()
        main_page.click_faq_question(index)
        actual_text = main_page.get_faq_answer_text(index)
        assert actual_text == expected_text
