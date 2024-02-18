from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# Locators for the Empty cart message
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
EMPTY_CART_MESSAGE = (By.XPATH, "//h1[text()='Your cart is empty']")

# Locators for the individual cart item
SEARCH_FIELD = (By.ID, "search")
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT = (By.XPATH, "//*[@data-test='resultsHeading']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*=addToCartButton]")
SIDE_NAVIGATION_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
SIDE_NAVIGATION_PRODUCT_NAME = (By.CSS_SELECTOR, "[class*='h-padding-l-tight'] h4")
VIEW_CART_AND_CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")
CART_SUMMARY = (By.CSS_SELECTOR, "div.h-margin-b-tight")
CART_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


search_word = "basket"  # search word
expected_cart_text = "1 item"  # Individual cart message
expected_empty_cart_text = "Your cart is empty"  # Empty cart message to verify


@given("Open target.com")
def open_target(context):
    context.driver.get("https://www.target.com")


@when("Enter the item in the search field and click")
def search_item(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BUTTON).click()


@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@when("Click on Add to cart")
def click_add_to_cart(context):
    sleep(6)
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when("Click on side navigation add to cart button")
def click_side_navigation_add_to_cart(context):
    context.wait.until((
        EC.element_to_be_clickable(SIDE_NAVIGATION_ADD_TO_CART_BTN)),
        message='Element is not located'
    )
    context.driver.find_element(*SIDE_NAVIGATION_ADD_TO_CART_BTN).click()


@when("Store product name")
def store_product_name(context):
    context.wait.until((
        EC.presence_of_element_located(SIDE_NAVIGATION_PRODUCT_NAME)),
        message='Element is not located'
    )
    context.product_name = context.driver.find_element(*SIDE_NAVIGATION_PRODUCT_NAME).text


@when("Click of View Cart and Checkout")
def click_on_view_cart_and_checkout(context):
    context.driver.find_element(*VIEW_CART_AND_CHECKOUT).click()


@then('Verify "Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    context.wait.until((
        EC.presence_of_element_located(EMPTY_CART_MESSAGE)),
        message="Element 'Empty message' is not located"
    )
    actual_text = context.driver.find_element(*EMPTY_CART_MESSAGE).text
    assert actual_text == expected_empty_cart_text, f"Expected {expected_empty_cart_text} but found {actual_text}"


@then("Verify search page is displayed")
def verify_search_result(context):
    context.wait.until((
        EC.presence_of_element_located(SEARCH_RESULT)),
        message="Search Result is not located."
    )
    actual_text = context.driver.find_element(*SEARCH_RESULT).text
    assert search_word in actual_text, f"The expected word '{search_word}' is not in the actual word '{actual_text}'"


@then("Verify the item is added to the cart")
def verify_item_added_to_cart(context):
    context.wait.until((
        EC.presence_of_element_located(CART_SUMMARY)),
        message='Cart Summary is not present'
    )
    actual_text = context.driver.find_element(*CART_SUMMARY).text
    assert expected_cart_text in actual_text, f"Expected text '{expected_cart_text}' not in '{actual_text}'"


@then("Verify cart has product name")
def verify_product_name(context):
    actual_product_name = context.driver.find_element(*CART_PRODUCT_NAME).text
    assert context.product_name == actual_product_name, f"Expected '{context.product_name}' but got '{actual_product_name}'"

