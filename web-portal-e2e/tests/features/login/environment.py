import os

from selenium import webdriver
from configparser import ConfigParser

from webportal.support import browser


def before_all(context):
    config = ConfigParser()
    setup_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(setup_file)

    context.browser = config.get('Environment', 'Browser')
    context.username = config.get('Account', 'Username')
    context.password = config.get('Account', 'Password')
    context.url = config.get('Local Host', 'Host')


def after_all(context):
    browser.close_browser()
