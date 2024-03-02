from behave import given, when, then
from selenium.webdriver.common.by import By

# Locators
TARGET_CIRCLE = (By.ID, "utilityNav-circle")
BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*='BenefitCard']")

CIRCLE_TABS = (By.CSS_SELECTOR, "class*='PageSelectionText'")


@given("Open Circle page")
def open_circle_page(context):
    context.app.circle_page.open_circle()


@given("Store original window")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when("Click on Target circle")
def click_target_circle(context):
    context.driver.find_element(*TARGET_CIRCLE).click()


@when("Click Google Play button")
def click_google_play_button(context):
    context.app.circle_page.click_google_play_button()


@when("Switch to new window")
def switch_to_new_window(context):
    context.app.page.switch_to_new_window()


@then("Verify there are {expected_elements} benefit boxes")
def verify_benefit_boxes(context, expected_elements):
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == int(expected_elements), f"Expected {expected_elements} boxes but got {len(benefit_boxes)}"


@then("Verify that clicking through Circle tabs works")
def verify_click_through_tabs(context):
    context.app.circle_page.verify_can_click_thru_tabs()


@then("Verify Google Play Target page opened")
def verify_google_play_target_opened(context):
    context.app.circle_page.google_play_opened()


@then("Close current page")
def close_current_page(context):
    context.driver.close()


@then("Return to original window")
def switch_to_original_window(context):
    context.app.circle_page.switch_to_window_by_id(context.original_window)
