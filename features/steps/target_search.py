from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_TEXT = (By.ID, "search")
SEARCH_BTN  = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[data-test='resultsHeading']")


@when("Enter {search_word} into search field")
def enter_search_word(context, search_word):
    context.driver.find_element(*SEARCH_TEXT).send_keys(search_word)


@when("Click on the search icon")
def click_on_search_btn(context):
    context.driver.find_element(*SEARCH_BTN).click()


@then("Search results for {search_result} are shown")
def verify_search_results(context, search_result):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert search_result in actual_text, f"Expected {search_result}, got {actual_text}"


@then("Search result page URL has search term {expected_partial_url}")
def verify_search_result_url(context, expected_partial_url):
    assert expected_partial_url in context.driver.current_url, f"Couldn't find the {expected_partial_url} in Current URL"
