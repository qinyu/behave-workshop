from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()
