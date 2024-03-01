from selenium.webdriver.common.by import By
from pages.base_page import Page


class SideNavigationPage(Page):
    SIDE_NAVIGATION_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def open_side_navigation_sign_in(self):
        self.wait_element_clickable_click(*self.SIDE_NAVIGATION_SIGN_IN)
