import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import LoginPageLocators, ItemPageLocators



class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_name_in_message(self):
        assert self.browser.find_element(*ItemPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE).text == self.browser.find_element(
            *ItemPageLocators.ITEM_NAME).text

    def should_be_correct_price_in_message(self):
        assert self.browser.find_element(
            *ItemPageLocators.BASKET_PRICE_MESSAGE).text == self.browser.find_element(
            *ItemPageLocators.ITEM_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ItemPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE), \
            "Success message is not disappeared, but should"
