from pages.login_page import LoginPage
from pages.locators import LoginPageLocators


def test_guest_should_be_on_the_login_page(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form_on_login_page(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_registration_form_on_login_page(browser):
    page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)
    page.open()
    page.should_be_register_form()
