from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartSummaryPage(Page):

    EMPTY_CART_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_empty_cart_summary(self):
        expected_empty_cart_text = "Your cart is empty"  # Empty cart message to verify
        # actual_text = self.driver.find_element(*self.EMPTY_CART_MESSAGE).text
        # assert actual_text == "Your cart is empty", f"Expected 'Your cart is empty' but found {actual_text}"
        self.verify_text(expected_empty_cart_text, *self.EMPTY_CART_MESSAGE)
