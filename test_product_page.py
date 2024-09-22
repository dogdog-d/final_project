from pages.product_page import ProductPage
from pages.backet_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ '

class TestGuestAddToBasketFromProductPage:
    # @pytest.mark.parametrize('link', [ # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                                   # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    #                                   ])

    def test_guest_can_add_product_to_basket(self, browser, link):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ '

        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name_in_message()
        page.should_be_correct_price_in_message()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.should_not_be_success_message()
        # test should fail

    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_success_message_disappear()
        # test should fail

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket_message()
        basket_page.should_not_be_basket_items()

class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name_in_message()
        page.should_be_correct_price_in_message()