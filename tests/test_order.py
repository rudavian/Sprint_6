import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    @allure.feature("Order")
    @allure.story("Позитивный сценарий заказа самоката")
    @allure.title("Проверка успешного создания заказа")
    @pytest.mark.parametrize(
        "entry_point, order_data",
        [
            (
                "header",
                {
                    "name": "Иван",
                    "surname": "Петров",
                    "address": "Москва, улица Пушкина, дом 10",
                    "metro_station": "Сокольники",
                    "phone": "+79990000001",
                    "delivery_date": "10.06.2026",
                    "rent_period": "сутки",
                    "color": "black",
                    "comment": "Позвонить за час",
                },
            ),
            (
                "footer",
                {
                    "name": "Анна",
                    "surname": "Смирнова",
                    "address": "Москва, улица Ленина, дом 5",
                    "metro_station": "Черкизовская",
                    "phone": "+79990000002",
                    "delivery_date": "11.06.2026",
                    "rent_period": "двое суток",
                    "color": "grey",
                    "comment": "Оставить у подъезда",
                },
            ),
        ],
    )
    def test_successful_order_creation(self, driver, entry_point, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies_if_present()
        main_page.open_order_form(entry_point)
        order_page.create_order(order_data)
        success_order_message = order_page.get_success_order_message()
        assert "Заказ оформлен" in success_order_message
