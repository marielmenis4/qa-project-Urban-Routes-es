import data
import pages
from pages import UrbanRoutesPage
from selenium import webdriver

from helpers import retrieve_phone_code

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
        routes_page.set_route(data.address_from, data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_button()
        # Verificar que el botón quedó activado
        assert self.driver.find_element(*routes_page.comfort_button).get_property('checked') is True

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_number(data.phone_number)  # dato real
        # Para verificar, obtener el texto del elemento que muestra el teléfono
        assert routes_page.get_phone_number() == data.phone_number

    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_card(data.card_number, data.card_code)
        # Verificar que el método de pago ahora muestra "Tarjeta"
        payment_text = routes_page.get_payment_method()
        assert 'Tarjeta' in payment_text or 'Card' in payment_text

    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.comment_for_driver(data.message_for_driver)
        # Verificar que el mensaje al conductor ahora muestra 'Muéstrame el camino al museo'
        message_text = routes_page.get_message_for_driver()
        assert 'Muéstrame el camino al museo' in message_text

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_tissue_blanket_button()
        # Verificar que el switch quedó activado
        assert self.driver.find_element(*routes_page.blanket_switch).get_property('checked') is True

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream(2)
        counter = self.driver.find_element(By.CLASS_NAME, 'counter-value').text
        assert counter == '2'

    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_find_taxi_button()
        routes_page.wait_for_load_order_header()
        # Si wait_for_load_order_header no lanza excepción, el modal apareció
        modal = self.driver.find_element(*routes_page.order_header)
        assert modal.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
