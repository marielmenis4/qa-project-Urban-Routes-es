from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import retrieve_phone_code
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    flash_button = (By.CSS_SELECTOR, "div.mode.active")
    ask_taxi_button = (By.CSS_SELECTOR, "button.button.round")

    comfort_button = (By.XPATH, ".//div[@tcard = 'Comfort']")

    phone_number_control = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
    phone_code_input = (By.ID, "code")
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")

    pay_button = (By.CLASS_NAME, "pp-value-container")
    card_button = (By.CSS_SELECTOR, ".pp-row.disabled")
    card_field = (By.CLASS_NAME, "pp-text")
    add_card = (By.CLASS_NAME, "card-input")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    submit_button = (By.XPATH, "//form[@name='button-full']//button[text()='Agregar']")
    exit_card_button = (By.CSS_SELECTOR, ".payment-picker.open .close-button")

    driver_message = (By.ID, "comment")

    blanket_switch = (By.CSS_SELECTOR, "input.switch-input")
    acoustic_curtain_button = (By.XPATH, "//div[contains(text(),'Cortina acústica')]/..//input[@class='switch-input']")
    ice_cream_button = (By.CLASS_NAME, "counter-plus")

    find_taxi_button = (By.CLASS_NAME, "smart-button-secondary")

    order_header = (By.CLASS_NAME, 'order-body')

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

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_control).click()
        self.driver.find_element(*self.phone_input).send_keys(phone_number)
        self.driver.find_element(*self.next_button).click()
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_code_input).send_keys(phone_code)
        self.driver.find_element(*self.confirm_button).click()  # 6. Confirmar
    def get_phone_number(self):
        return self.driver.find_element(By.CLASS_NAME, 'np-text').text

    def fill_card(self, card_number, card_code):
        self.driver.find_element(*self.pay_button).click()
        self.driver.find_element(*self.card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.card_code_field).send_keys(card_code)
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)  # quitar foco ✅
        self.driver.find_element(*self.submit_button).click()
        self.driver.find_element(*self.exit_card_button).click()
    def get_payment_method(self):
        return self.driver.find_element(By.CLASS_NAME, 'pp-value-text').text

    def set_driver_message(self, message_for_driver):
        self.driver.find_element(*self.driver_message).send_keys(message_for_driver)
    def get_message_for_driver(self):
        return self.driver.find_element(*self.driver_message).get_property('value')

    def click_tissue_blanket_button(self):
        self.driver.find_element(*self.blanket_switch).click()
    def click_acoustic_curtain_button(self):
        self.driver.find_element(*self.acoustic_curtain_button).click()
    def add_ice_cream(self, times=2):
        button = self.driver.find_element(*self.ice_cream_button)
        for _ in range(times):
            button.click()
    def click_find_taxi_button(self):
        self.driver.find_element(*self.find_taxi_button).click()

    def wait_for_load_order_header(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.order_header))
