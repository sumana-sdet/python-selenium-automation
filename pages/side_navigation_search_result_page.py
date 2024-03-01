from selenium.webdriver.common.by import By

from pages.base_page import Page


class SideNavigationSearchResultPage(Page):

    SIDE_NAVIGATION_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
    SIDE_NAVIGATION_PRODUCT_NAME = (By.CSS_SELECTOR, "[class*='h-padding-l-tight'] h4")
    VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")

    def click_side_navigation_add_to_cart(self):
        self.wait_element_clickable_click(*self.SIDE_NAVIGATION_ADD_TO_CART_BTN)

    def get_product_name(self):
        self.wait_element_visible(*self.SIDE_NAVIGATION_PRODUCT_NAME)
        return self.find_element(*self.SIDE_NAVIGATION_PRODUCT_NAME).text

    def click_view_cart_and_checkout(self):
        self.wait_element_clickable_click(*self.VIEW_CART_AND_CHECKOUT)
