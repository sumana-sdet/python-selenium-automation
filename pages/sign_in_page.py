from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")
    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_WITH_PASSWORD = (By.ID, "login")

    def verify_sign_in_page_open(self):
        self.wait_element_visible(*self.SIGN_IN_HEADER)
        actual_text = self.find_element(*self.SIGN_IN_HEADER).text
        assert "sign in" in actual_text.lower(), f"Expected page is not displayed"
        assert self.find_element(*self.EMAIL_FIELD).is_displayed(), f"Expected email field not displayed"

    def enter_email_password(self):
        self.input_text("raisadvorak@joopeerr.com", *self.EMAIL_FIELD)
        self.input_text("*********", *self.PASSWORD_FIELD)

    def click_sign_in_button(self):
        self.wait_element_clickable_click(*self.SIGN_IN_WITH_PASSWORD)

    def verify_user_logged_in(self):
        self.wait_element_invisible(*self.SIGN_IN_HEADER)



