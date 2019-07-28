from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def product_name_on_capture_is_equal_for_real(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ALERT).text
        assert product_name == message, \
            'Different product names on the page and pop-up message'

    def product_price_in_cart_same_as_on_product_page(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == cart_price, \
            'Different price on the page and cart'

    def add_to_cart_messages(self):
        self.product_price_in_cart_same_as_on_product_page()
        self.product_name_on_capture_is_equal_for_real()



