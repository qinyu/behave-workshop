from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from pages import LoginPage


@given(u'I open wordpress')
def step_impl(context):
    context.driver.get("http://mywp-1-qinyu.tenxapp.com")


@when(u'I click "login"')
def step_impl(context):
    if context.config.userdata.get("platform", "firefox") == 'android_chrome':
        context.driver.find_element_by_css_selector("button.secondary-toggle").click()
    context.driver.find_element_by_partial_link_text("Log in").click()


@then(u'I can see login page')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Lost your password?")))
    assert context.driver.find_element_by_partial_link_text("Lost your password?") is not None


@when(u'I login with credential "{user}" and "{password}"')
def step_impl(context, user, password):
    LoginPage(context.driver).login_with_credential(user, password)
    # context.driver.find_element_by_id('user_login').send_keys(user)
    # if password != "N/A":
    #     context.driver.find_element_by_id('user_pass').send_keys(password)
    # context.driver.find_element_by_id('wp-submit').click()


@then(u'I can login successful')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        lambda driver: driver.current_url == 'http://mywp-1-qinyu.tenxapp.com/wp-admin/')


@then(u'I should see error message "{error}"')
def step_impl(context, error):
    # assert context.driver.find_element_by_id('login_error').text == error
    assert LoginPage(context.driver).get_login_error() == error
