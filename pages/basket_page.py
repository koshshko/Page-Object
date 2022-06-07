from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def empty_basket_tests(self):
        self.basket_should_be_empty()
        self.basket_is_empty_message()

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket might have products added"

    def basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket might not be empty"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"