from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DELIVERY_DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_ORDER_MESSAGE = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")

    @staticmethod
    def metro_station(station_name):
        return (By.XPATH, f".//div[contains(@class, 'select-search__select')]//div[text()='{station_name}']")

    @staticmethod
    def rent_period(period):
        return (By.XPATH, f".//div[contains(@class, 'Dropdown-option') and text()='{period}']")
