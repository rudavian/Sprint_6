import allure

from pages.main_page import MAIN_PAGE_URL, MainPage


@allure.feature("Logo redirects")
class TestLogoRedirects:
    @allure.story("Логотип Самоката")
    @allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies_if_present()
        main_page.open_order_form_and_click_scooter_logo()
        current_url = main_page.get_current_url()
        assert current_url == MAIN_PAGE_URL

    @allure.story("Логотип Яндекса")
    @allure.title("Проверка открытия Дзена в новом окне по клику на логотип Яндекса")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies_if_present()
        main_page.click_yandex_logo_and_switch_to_new_window()
        main_page.wait_for_url_contains("dzen.ru")
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url
