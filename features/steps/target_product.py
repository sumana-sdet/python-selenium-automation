from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_OPTIONS = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given("Open target product {product_id} page")
def open_target_product(context, product_id):
    context.driver.get(f"https://www.target.com/p/{product_id}")


@then("Verify user can click through {list_of_colors}")
def verify_colors(context, list_of_colors):
    expected_colors = []
    for color in list_of_colors.split(","):
        expected_colors.append(color)
    actual_colors = []

    context.wait.until((
        EC.presence_of_element_located(COLOR_OPTIONS)),
        message=f"Element is not located!"
    )
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_OPTIONS).text
        selected_color = selected_color.split("\n")[1]
        actual_colors.append(selected_color)
        print(actual_colors)


# @then("Verify user can click through colors")
# def verify_colors(context):
#     expected_colors = ["Black", "Brown", "Cream", "Dark Gray", "Green", "Light Green", "Tan"]
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)
#     for color in colors:
#         color.click()
#         selected_color = context.driver.find_element(*SELECTED_OPTIONS).text
#         selected_color = selected_color.split("\n")[1]
#         actual_colors.append(selected_color)
#         print(actual_colors)


PRODUCTS_PER_PAGE = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")


@then("Verify every product on Target Search results page has product name and product image")
def verify_product_details(context):
    # java script to scroll all products
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")

    products = context.driver.find_elements(*PRODUCTS_PER_PAGE)
    # print(len(products))
    for product in products:
        assert context.driver.find_element(*PRODUCT_IMAGE).is_displayed(), f"Product image not displayed"
        assert context.driver.find_element(*PRODUCT_TITLE).is_displayed(), f"Product title not displayed"
