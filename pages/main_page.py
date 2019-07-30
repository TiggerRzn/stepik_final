from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def cart_message(self):
        basket_message = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE).text
        assert 'empty' in basket_message, 'The cart is not empty'
