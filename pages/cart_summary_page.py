from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartSummaryPage(Page):

    EMPTY_CART_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")
    CART_SUMMARY = (By.CSS_SELECTOR, "div.h-margin-b-tight")
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_empty_cart_summary(self):
        expected_empty_cart_text = "Your cart is empty"  # Empty cart message to verify
        # actual_text = self.driver.find_element(*self.EMPTY_CART_MESSAGE).text
        # assert actual_text == "Your cart is empty", f"Expected 'Your cart is empty' but found {actual_text}"
        self.verify_text(expected_empty_cart_text, *self.EMPTY_CART_MESSAGE)

    def verify_item_added_to_cart(self):
        self.wait_element_visible(*self.CART_SUMMARY)
        self.verify_partial_text("1 item", *self.CART_SUMMARY)

    def verify_product_name(self, product_name):
        self.verify_text(product_name, *self.CART_PRODUCT_NAME)
