import pytest
from pages.main_page import MainPage
from pages.locators import BasePageLocators
from pages.cart_page import CartPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, BasePageLocators.MAIN_PAGE_URL)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, BasePageLocators.MAIN_PAGE_URL)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = CartPage(browser, BasePageLocators.MAIN_PAGE_URL)
    page.open()
    page.go_to_cart()
    page.should_not_be_item_in_the_cart()
    page.cart_message()



