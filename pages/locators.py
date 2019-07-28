from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com "


class LoginPageLocators(object):
    LOGIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators(object):
    PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADD_TO_CART_ALERT = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini p")
    PROMO_LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

