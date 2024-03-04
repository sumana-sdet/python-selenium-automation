from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
# SIDE_NAVIGATION_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
# SIGN_IN_HEADER = (By.XPATH, "//span[text()='Sign into your Target account']")
# EMAIL_FIELD = (By.ID, "username")


@when("Click Sign In")
def click_sign_in(context):
    # context.driver.find_element(*SIGN_IN).click()
    context.app.header.click_on_signin()


@when("From right side navigation menu, click Sign In")
def click_side_navigation_sign_in(context):
    # context.driver.find_element(*SIDE_NAVIGATION_SIGN_IN).click()
    context.app.side_navigation_page.open_side_navigation_sign_in()


@then("Verify Sign In form opened")
def verify_signin_form(context):
    # context.wait.until((
    #     EC.visibility_of_element_located(SIGN_IN_HEADER)),
    #     message="Sign in header can't be located."
    # )
    # actual_text = context.driver.find_element(*SIGN_IN_HEADER).text
    # assert "sign in" in actual_text.lower(), f"Expected page is not displayed"
    # assert context.driver.find_element(*EMAIL_FIELD).is_displayed(), f"Expected email field not displayed"
    context.app.sign_in_page.verify_sign_in_page_open()


@when("Input email and password on SignIn page")
def input_email_password(context):
    context.app.sign_in_page.enter_email_password()


@when("Click on Sign In Button")
def click_sign_in_btn(context):
    context.app.sign_in_page.click_sign_in_button()


@then("Verify user is logged in")
def verify_user_logged_in(context):
    context.app.sign_in_page.verify_user_logged_in()


@when("Click on Target Terms and conditions link")
def click_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_and_conditions()


@then("Verify Terms and Conditions page is opened")
def verify_terms_and_conditions_page_opened(context):
    context.app.sign_in_page.verify_terms_and_conditions_page_opened()


@then("Verify that “We can't find your account.” message is shown")
def verify_incorrect_login_message(context):
    context.app.sign_in_page.verify_incorrect_login_message()