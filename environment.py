import os

from selenium import webdriver


def before_scenario(context, scenario):
    platform = context.config.userdata.get("platform", "firefox")
    if platform == 'android_chrome':
        caps = {
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': '84B5T15A17002528',  # change to your our device serial id
            'browserName': 'Chrome'
        }
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    elif platform == 'firefox':
        context.driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(), 'geckodriver'))
        context.driver.maximize_window()
    else:
        context.driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
        context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()
