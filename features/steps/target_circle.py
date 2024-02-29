from behave import given, when, then
from selenium.webdriver.common.by import By

# Locators
TARGET_CIRCLE = (By.ID, "utilityNav-circle")
BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*='BenefitCard']")

CIRCLE_TABS = (By.CSS_SELECTOR, "class*='PageSelectionText'")


@given("Open Circle page")
def open_circle_page(context):
    context.app.circle_page.open_circle()


@when("Click on Target circle")
def click_target_circle(context):
    context.driver.find_element(*TARGET_CIRCLE).click()


@then("Verify there are {expected_elements} benefit boxes")
def verify_benefit_boxes(context, expected_elements):
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == int(expected_elements), f"Expected {expected_elements} boxes but got {len(benefit_boxes)}"


@then("Verify that clicking through Circle tabs works")
def verify_click_through_tabs(context):
    context.app.circle_page.verify_can_click_thru_tabs()
