from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a[href$='/basket/']:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_PRODUCT_ADDED = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    ALERT_PRODUCT_ADDED_INNER_TXT = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    ALERT_CART_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3)")
    ALERT_CART_PRICE_TXT = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner strong")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TXT = (By.CSS_SELECTOR, "#content_inner p:nth-child(1)")
