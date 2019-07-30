import time
from pages.main_page import MainPage
from pages.locators import BasePageLocators


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, BasePageLocators.MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, BasePageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, BasePageLocators.MAIN_PAGE_URL)
    page.open()
    page.go_to_cart()
    # page.is_not_element_present()
    page.cart_message()



