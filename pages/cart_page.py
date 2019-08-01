from pages.base_page import BasePage
from pages.locators import *


class CartPage (BasePage):
    def cart_message(self):
        basket_message = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE).text
        assert 'empty' in basket_message, 'The cart is not empty'

    def should_not_be_item_in_the_cart(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), \
            'There is "empty basket" message, but should not'

    def should_be_item_in_the_cart(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_MESSAGE), \
            '"Empty basket" message is not present'
