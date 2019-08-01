import time
import faker
from pages.cart_page import CartPage
from pages.locators import *
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ProductPageLocators.PROMO_LINKS)
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.add_to_cart_messages()


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    product_page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_cart(browser):
    product_page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
    product_page.open()
    product_page.add_to_cart()
    time.sleep(1)
    product_page.should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en" \
           "-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
    page.open()
    page.go_to_cart()
    cart_item = CartPage(browser, BasePageLocators.BASKET_MESSAGE)
    cart_item.should_not_be_item_in_the_cart()
    cart_item.cart_message()


@pytest.mark.registration
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        # Generation of user email & password
        f = faker.Faker()
        email = f.email()
        password = f.password()

        # open registration page
        page = LoginPage(browser,
                         'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        page.open()

        # activate registration function from login_page.py
        page.register_new_user(email, password)

        # activate user image checking function from login_page.py
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_cart(self, browser):
        product_page = ProductPage(browser, ProductPageLocators.PRODUCT_PAGE_URL)
        product_page.open()
        product_page.add_to_cart()
        product_page.add_to_cart_messages()


