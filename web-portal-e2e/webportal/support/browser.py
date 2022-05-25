from webportal.support import factory
from webportal.common import config
from webportal.helper.wait import wait_for
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def get_driver():
    return factory.get_shared_driver()


def get_title():
    return get_driver().title


def maximize_browser():
    get_driver().maximize_window()


def open_url(url):
    get_driver().get(url)


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all_browsers():
    factory.quit_all_browsers()


def start_driver(name, key="default"):
    factory.start_driver(name, key)


def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = config.timeout
    if polling is None:
        polling = config.poll_during_waits

    return wait_for(get_driver(), webdriver_condition, timeout, polling)
