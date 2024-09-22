from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ItemPageLocators:
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") # 9,99 £
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1") # The shellcoder's handbook
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong") # The shellcoder's handbook
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p:nth-child(1) strong") #59,96 £


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")



