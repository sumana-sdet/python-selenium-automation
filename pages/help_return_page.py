from selenium.webdriver.support.select import Select

from pages.base_page import Page
from selenium.webdriver.common.by import By

class HelpReturnPage(Page):

    RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    HELP_TOPICS = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    # PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_TEXT}']")

    # Dynamic locator
    def _get_header_locator(self, expected_header_text):
        return[self.HEADER[0], self.HEADER[1].replace("{HEADER_TEXT}", expected_header_text) ]

    def open_help_return_page(self):
        self.open("https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=")

    def verify_help_returns_opened(self):
        self.wait_element_visible(*self.RETURNS_HEADER)

    def select_help_topic(self, help_topic):
        topic_id = self.find_element(*self.HELP_TOPICS)
        select = Select(topic_id)
        select.select_by_value(help_topic)

    def verify_promotions_opened(self):
        self.wait_element_visible(*self.PROMOTIONS_HEADER)

    def verify_header(self, expected_header):
        locator = self._get_header_locator(expected_header)
        self.wait_element_visible(*locator)