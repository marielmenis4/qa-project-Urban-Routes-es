from selenium.webdriver.common.by import By

from pages import UrbanRoutesPage
from helpers import retrieve_phone_code

class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    flash_button = (By.CSS_SELECTOR, "div.mode.active")
    ask_taxi_button = (By.CSS_SELECTOR, "button.button.round")

    comfort_button = (By.CLASS_NAME, "tariff-card-4")

    phone_field = (By.CLASS_NAME, "np-text")

    pay_button = (By.CLASS_NAME, "pp-value-container")
    card_button = By.CLASS_NAME, "pp-row disabled"
    card_field = (By.CLASS_NAME, "pp-text")
    add_card = (By.CLASS_NAME, "card-input")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    submit_button = (By.XPATH, "//form[@name='button-full']//button[text()='Agregar']")
    exit_card_button = (By.TAG_NAME, "button")

    driver_message = (By.ID, "comment")

    blanket_switch = (By.CSS_SELECTOR, "input.switch-input")
    acoustic_curtain_button = (By.CSS_SELECTOR, "input.switch-input")
    ice_cream_button = (By.CLASS_NAME, "counter-plus")

    find_taxi_button = (By.CLASS_NAME, "smart-button-secondary")

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)
        self.click_ask_taxi_button()

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_flash_button(self):
        self.driver.find_element(*self.flash_button).click()
    def click_ask_taxi_button(self):
        self.driver.find_element(*self.ask_taxi_button).click()
    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()
    def set_phone(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)
    def click_pay_button(self):
        self.driver.find_element(*self.pay_button).click()
    def click_card_button(self):
        self.driver.find_element(*self.card_button).click()
    def set_card(self, card_number):
        self.driver.find_element(*self.card_field).send_keys(card_number)
    def set_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)
    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()
    def click_exit_card_button(self):
        self.driver.find_element(*self.exit_card_button).click()
    def set_driver_message(self, message_for_driver):
        self.driver.find_element(*self.driver_message).send_keys(message_for_driver)
    def click_tissue_blanket_button(self):
        self.driver.find_element(*self.tissue_blanket_button).click()
    def click_acoustic_curtain_button(self):
        self.driver.find_element(*self.acoustic_curtain_button).click()
    def add_ice_cream(self, times=2):
        button = self.driver.find_element(*self.ice_cream_button)
        for _ in range(times):
            button.click()
    def click_find_taxi_button(self):
        self.driver.find_element(*self.find_taxi_button).click()
    def wait_for_load_order_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order-header-title))
