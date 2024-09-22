import time

from .base_page import BasePage
from .locators import LoginPageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.url, "basket is absent in current url"

    def should_be_empty_basket_message(self):
        assert 'Your basket is empty.' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"
