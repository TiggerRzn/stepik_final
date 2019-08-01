import faker
from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form is not present'

    # fake credentials creating
    f = faker.Faker()
    email = f.email()
    password = f.password()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)

        registration_submit_button = self.browser.find_element(*RegisterPageLocators.REGISTRATION_BUTTON)
        registration_submit_button.click()
