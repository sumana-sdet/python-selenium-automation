from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # SWITCHING TO FIREFOX BROWSER
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # OTHER BROWSERS
    # service = Service(executable_path="absolute path of browser exe")
    # context.driver = webdriver.Firefox(service=service)

    # SAFARI BROWSERS
    # only on macOS. Safari already has setting in place so no need to set up the path or service.
    # Disadvantages: Less friendly than other browsers as it doesn't support all selenium commands
    # it is lower than other like we need to put more wait or sleep time.
    # context.driver = webdriver.Safari()

    # HEADLESS BROWSER
    # Headless browser means it connects to your browser at backend but doesn't show the visual interface
    # safari doesn't support headless, to enable do following
    # safari ->preferences->advance->enable-show feature for web developers: this adds a Develop in menu
    # safari-> Develop->Developer settings->Allow remote automation
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    ### BROWSERSTACK - CLOUD TESTING ###
    # Register for BrowserStack, then grab it from "access key"
    # bs_user = 'sumana_nAydHT'
    # bs_key = 'uMvuqzx4h3fPAjkSXbeu'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()

    # implicit wait
    # context.driver.implicitly_wait(4)

    # explicit wait
    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot('step_failed_{step}.png')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
