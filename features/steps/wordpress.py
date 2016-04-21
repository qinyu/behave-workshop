from behave import given, when, then
from selenium import webdriver


@given(u'I open wordpress')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("http://qinyu-my-wordpress.daoapp.io")


@when(u'I click "login"')
def step_impl(context):
    context.driver.find_element_by_partial_link_text("Log in").click()


@then(u'I can see login page')
def step_impl(context):
    assert context.driver.find_element_by_partial_link_text("Lost your password?") is not None
    context.driver.quit()
