from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.wait_for_clickable(locator).click()

    def send_keys_to_element(self, locator, text):
        self.wait_for_visible(locator).send_keys(text)

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_url_contains(self, text):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.url_contains(text)
        )

    def clear_and_send_keys(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def click_body(self):
        self.click_element(BasePageLocators.BODY)

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return self.driver.window_handles

    def wait_for_new_window(self, expected_windows_count):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.number_of_windows_to_be(expected_windows_count)
        )

    def switch_to_last_window(self):
        window_handles = self.get_window_handles()
        self.driver.switch_to.window(window_handles[-1])
