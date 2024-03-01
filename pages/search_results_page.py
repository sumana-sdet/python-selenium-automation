from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*=addToCartButton]")

    def verify_search_results_correct(self, search_word):
        # actual_text = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        # assert search_word in actual_text, f"Expected word {search_word} not in {actual_text}"
        self.wait_element_visible(*self.SEARCH_RESULT_HEADER)
        self.verify_partial_text(search_word, *self.SEARCH_RESULT_HEADER)

    def verify_search_results_url(self, expected_partial_url):
        # url = self.driver.current_url
        # assert expected_partial_url in url, f"Expected word {expected_partial_url} not in {url}"
        self.verify_partial_url(expected_partial_url)

    def click_add_to_cart(self):
        sleep(6)
        self.wait_element_clickable_click(*self.ADD_TO_CART_BTN)