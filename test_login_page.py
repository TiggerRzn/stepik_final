from pages.LoginPage import LoginPage
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
#
# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, MainPageLocators.MAIN_PAGE_LINK)
#     page.open()
#     page.go_to_login_page()

    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()
    #
    # def should_be_login_url(self):
    #     self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    #     assert True
    #
    # def should_be_login_form(self):
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'
    #
    # def should_be_register_form(self):
    #     assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is not present'
