from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage(BasePage):
    def open_main_page(self):
        self.open(MAIN_PAGE_URL)

    def accept_cookies_if_present(self):
        buttons = self.find_elements(MainPageLocators.COOKIE_BUTTON)
        if buttons:
            buttons[0].click()

    def click_order_button_in_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)

    def click_order_button_in_footer(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_IN_FOOTER)
        self.click_element(MainPageLocators.ORDER_BUTTON_IN_FOOTER)

    def open_order_form(self, entry_point):
        entry_points = {
            "header": self.click_order_button_in_header,
            "footer": self.click_order_button_in_footer,
        }
        entry_points[entry_point]()

    def click_faq_question(self, index):
        self.scroll_to_element(MainPageLocators.faq_question(index))
        self.click_element(MainPageLocators.faq_question(index))

    def get_faq_answer_text(self, index):
        return self.wait_for_visible(MainPageLocators.faq_answer(index)).text

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def open_order_form_and_click_scooter_logo(self):
        self.open_order_form("header")
        self.click_scooter_logo()

    def click_yandex_logo_and_switch_to_new_window(self):
        windows_count = len(self.get_window_handles())
        self.click_yandex_logo()
        self.wait_for_new_window(windows_count + 1)
        self.switch_to_last_window()
