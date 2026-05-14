import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    flash_button = (By.CLASS_NAME, "div.mode.active")
    ask_taxi_button = (By.CLASS_NAME, "button.button.round")
    comfort_button = (By.CLASS_NAME, "tariff-card-4")
    phone_field = (By.CLASS_NAME, "np-text")
    card_field = (By.CLASS_NAME, "pp-text")
    add_card = (By.CLASS_NAME, "card-input")
    card_number = (By.CLASS_NAME, "card-input")
    card_code = (By.ID, "code")
    submit_button = (By.XPATH, "//form[@name='button-full']//button[text()='Agregar']")
    exit_card_button = (By.TAG_NAME, "close-button")
    driver_message = (By.ID, "comment")
    tissue_blanket_button = (By.CSS_SELECTOR, "input.switch-input")
    acoustic_curtain_button = (By.CSS_SELECTOR, "input.switch-input")
    ice_button = (By.CSS_SELECTOR, "input.switch-input")
    find_taxi_button = (By.CLASS_NAME, "smart-button-secondary")

    def __init__(self, driver):
        self.driver = driver

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
        self.driver.find_element(*self.code_field).send_keys(card_code)
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
    def click_ice_button(self):
        self.driver.find_element(*self.ice_button).click().click()
    def click_find_taxi_button(self):
        self.driver.find_element(*self.find_taxi_button).click()
    def wait_for_load_order_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order-header-title))

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
