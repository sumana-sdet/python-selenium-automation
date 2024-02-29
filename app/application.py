from pages.base_page import Page
from pages.cart_summary_page import CartSummaryPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_summary_page = CartSummaryPage(driver)
        self.circle_page = CirclePage(driver)

