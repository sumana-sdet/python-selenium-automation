from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
    context.wait.until((
        EC.visibility_of_element_located(SIGN_IN_HEADER)),
        message="Sign in header can't be located."
    )
    actual_text = context.driver.find_element(*SIGN_IN_HEADER).text
    assert "sign in" in actual_text.lower(), f"Expected page is not displayed"
    assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), f"Expected email field not displayed"
