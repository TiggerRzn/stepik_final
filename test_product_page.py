from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ProductPageLocators.PROMO_LINKS)
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.add_to_cart_messages()



