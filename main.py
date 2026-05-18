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

    def test_ask_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        flash_button = pages.flash_button
        ask_taxi_button = pages.ask_taxi_button
        routes_page.ask_taxi(pages.flash_button, pages.ask_taxi_button)
        assert routes_page.get_flash() == pages.flash_button
        assert routes_page.get_taxi() == pages.ask_taxi_button

    def test_taxi_type(self):
        routes_page = UrbanRoutesPage(self.driver)
        comfort_button = pages.comfort_button
        routes_page.taxi_type(pages.comfort_button)
        assert routes_page.get_comfort() == pages.comfort_button

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_number(data.phone_number)  # dato real
        # Para verificar, obtener el texto del elemento que muestra el teléfono
        assert routes_page.get_phone_number() == data.phone_number

    def test_set_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        pay_button = pages.pay_button
        card_button = pages.card_button
        card_field = pages.card_field
        add_card = pages.add_card
        card_number_field = pages.card_number_field
        card_code_field = pages.card_code_field
        submit_button = pages.submit_button
        exit_card_button = pages.exit_card_button
        routes_page.set_card(pages.pay_button, pages.card_button, pages.card_field, pages.add_card, pages.card_number_field, pages.card_code_field, pages.submit_button, pages.exit_card_button)
        assert routes_page.get_pay_button() == pages.pay_button
        assert routes_page.get_card_button() == pages.card_button
        assert routes_page.get_card_field() == pages.card_field
        assert routes_page.get_add_card() == pages.add_card
        assert routes_page.get_card_number() == pages.card_number_field
        assert routes_page.get_card_code() == pages.card_code_field
        assert routes_page.get_submit() == pages.submit_button
        assert routes_page.get_exit() == pages.exit_card_button

    def test_set_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        driver_message = pages.driver_message
        routes_page.set_message(pages.driver_message)
        assert routes_page.get_messsage() == pages.driver_message

    def test_set_amenities(self):
        routes_page = UrbanRoutesPage(self.driver)
        blanket_switch = pages.blanket_switch
        acoustic_curtain_button = pages.acoustic_curtain_button
        ice_cream_button = pages.ice_cream_button
        routes_page.set_amenities(pages.blanket_switch, pages.acoustic_curtain_button, pages.ice_cream_button)
        assert routes_page.get_blancket() == pages.blanket_switch
        assert routes_page.get_acoustic_curtain() == pages.acoustic_curtain_button
        assert routes_page.get_ice_cream() == pages.ice_cream_button

    def test_find_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        find_taxi_button = pages.find_taxi_button
        routes_page.set_find_taxi(pages.find_taxi_button)
        assert routes_page.get_find_taxi() == pages.find_taxi_button

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
