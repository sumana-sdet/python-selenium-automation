from behave import given, when, then
from selenium.webdriver.common.by import By

# Locators
TARGET_CIRCLE = (By.ID, "utilityNav-circle")
BENEFIT_BOXES = (By.CSS_SELECTOR, "[class*='BenefitsGrid'] li")

TARGET_TITLE = (By.CSS_SELECTOR, "[title='Help']")
TARGET_HELP = (By.CSS_SELECTOR, "[class='custom-h2']")
TARGET_HELP_SEARCH = (By.CSS_SELECTOR, "[class='form-search form-inline'] input")
TARGET_LIKE_HEADER = (By.XPATH, "//h2[text()='What would you like to do?']")
TARGET_LIKE_TO_DO = (By.CSS_SELECTOR, "[class='col-lg-12'] div.grid_6")
TARGET_CONTACT = (By.CSS_SELECTOR, "[class='col-lg-12'] div[class*='grid_4']")
TARGET_BROWSE_HELP_PAGES = (By.XPATH, "//h2[text()='Browse all Help pages']")


@given("Open https://help.target.com/help")
def open_target(context):
    context.driver.get("https://help.target.com/help")


@then("Verify Target Help page is opened")
def verify_target_help_page(context):
    actual_text = context.driver.find_element(*TARGET_TITLE).text
    assert actual_text == 'Help', f"Expected text didn't match {actual_text}"


@then("Verify Target Help Logo is present")
def verify_target_help_logo(context):
    actual_text = context.driver.find_element(*TARGET_HELP).text
    assert actual_text == 'Target Help', f"Expected text didn't match {actual_text}"


@then("Verify Search Text field has {no_of_elements} elements")
def verify_search_text_field(context, no_of_elements):
    search = context.driver.find_elements(*TARGET_HELP_SEARCH)
    assert len(search) == int(no_of_elements), f"Expected {no_of_elements} elements but found {len(search)} elements"


@then("Verify header 'What would you like field' displayed")
def verify_like_header(context):
    actual_text = context.driver.find_element(*TARGET_LIKE_HEADER).text
    assert actual_text == 'What would you like to do?', f"Expected text didn't match {actual_text}"


@then("Verify 'What would you like field' has {no_of_elements} elements")
def verify_like_to_do_elements(context, no_of_elements):
    likes = context.driver.find_elements(*TARGET_LIKE_TO_DO)
    assert len(likes) == int(no_of_elements), f"Expected {no_of_elements} elements but found {len(likes)} elements"


@then("Verify Contact block has {no_of_elements} elements")
def verify_contact_elements(context, no_of_elements):
    contact = context.driver.find_elements(*TARGET_CONTACT)
    assert len(contact) == int(no_of_elements), f"Expected {no_of_elements} elements but found {len(contact)} elements"


@then("Verify header 'Browse all Help pages'")
def verify_browser_help_header(context):
    actual_text = context.driver.find_element(*TARGET_BROWSE_HELP_PAGES).text
    assert actual_text == 'Browse all Help pages', f"Expected text didn't match {actual_text}"
