from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_IN_HEADER = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_IN_FOOTER = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def faq_answer(index):
        return (By.XPATH, f".//*[@id='accordion__panel-{index}']/p")
