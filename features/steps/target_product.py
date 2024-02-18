from behave import given, when, then
from selenium.webdriver.common.by import By


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_OPTIONS = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

@given("Open target product {product_id} page")
def open_target_product(context, product_id):
    context.driver.get(f"https://www.target.com/p/{product_id}")


@then("Verify user can click through colors")
def verify_colors(context):
    expected_colors = ["Black", "Brown", "Cream", "Dark Gray", "Green", "Light Green", "Tan"]
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_OPTIONS).text
        selected_color = selected_color.split("\n")[1]
        actual_colors.append(selected_color)
        print(actual_colors)
