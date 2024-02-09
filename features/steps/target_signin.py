from behave import given, when, then
from selenium.webdriver.common.by import By

SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIDE_NAVIGATION_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
SIGN_IN_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")
EMAIL_FIELD = (By.ID, "username")


@when("Click Sign In")
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN).click()


@when("From right side navigation menu, click Sign In")
def click_side_navigation_sign_in(context):
    context.driver.find_element(*SIDE_NAVIGATION_SIGN_IN).click()


@then("Verify Sign In form opened")
def verify_signin_form(context):
    actual_text = context.driver.find_element(*SIGN_IN_HEADER).text
    assert "sign in" in actual_text.lower(), f"Expected page is not displayed"
    assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), f"Expected email field not displayed"
