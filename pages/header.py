from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_on_cart(self):
       # self.click(*self.CART_ICON)
       self.wait_element_clickable_click(*self.CART_ICON)

    def click_on_signin(self):
        self.wait_element_clickable_click(*self.SIGN_IN)

    def hover_signin_btn(self):
        sign_in_btn = self.find_element(*self.SIGN_IN)
        actions = ActionChains(self.driver)
        actions.move_to_element(sign_in_btn)
        actions.perform()

    def verify_signin_arrow(self):
        self.wait_element_visible(*self.SIGN_IN_ARROW)