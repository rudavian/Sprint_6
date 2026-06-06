import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить первую форму заказа")
    def fill_first_order_form(self, name, surname, address, metro_station, phone):
        self.clear_and_send_keys(OrderPageLocators.NAME_INPUT, name)
        self.clear_and_send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.clear_and_send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.clear_and_send_keys(OrderPageLocators.METRO_INPUT, metro_station)
        self.click_element(OrderPageLocators.metro_station(metro_station))
        self.clear_and_send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_order_form(self, delivery_date, rent_period, color, comment):
        self.clear_and_send_keys(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)
        self.click_body()
        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.rent_period(rent_period))
        color_locators = {
            "black": OrderPageLocators.BLACK_COLOR_CHECKBOX,
            "grey": OrderPageLocators.GREY_COLOR_CHECKBOX,
        }
        self.click_element(color_locators[color])
        self.clear_and_send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажать кнопку Заказать")
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_order_message(self):
        return self.wait_for_visible(OrderPageLocators.SUCCESS_ORDER_MESSAGE).text

    @allure.step("Создать заказ")
    def create_order(self, order_data):
        self.fill_first_order_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"],
        )
        self.click_next_button()
        self.fill_second_order_form(
            order_data["delivery_date"],
            order_data["rent_period"],
            order_data["color"],
            order_data["comment"],
        )
        self.submit_order()
        self.confirm_order()
