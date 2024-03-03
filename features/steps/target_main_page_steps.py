from behave import given, when, then
from selenium.webdriver.common.by import By


@when("Hover over signin")
def hover_signin_btn(context):
    context.app.header.hover_signin_btn()


@then("Verify signin arrow shown")
def verify_signin_arrow(context):
    context.app.header.verify_signin_arrow()