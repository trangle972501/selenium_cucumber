from behave import given, when, then
from webportal.element.element import Element

from webportal.element.text_box import TextBox
from webportal.element.button import Button
from webportal.element.element import Element

from webportal.support.conditions import be, have
from webportal.support import browser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

_txt_search = TextBox("name=q")
_txt_username = TextBox("//input[contains(@class, 'input-login-uname')]")
_txt_password = TextBox("//input[contains(@class, 'input-login-pwd')]")
_btn_Login = Button("//button[@class='btn-login']")
_link_slide_list = Element("//div[@class='side-menu-side-list']/a")


@given('I am on the Fibers Digitalization Platform login page')
def step_impl(context):
    browser.start_driver(context.browser)
    browser.maximize_browser()
    browser.open_url(context.url)


@given('I am on Google page')
def step_impl(context):
    browser.start_driver("chrome")
    browser.maximize_browser()
    browser.open_url(context.url)


@when('I search {keyword} google')
def step_impl(context, keyword):
    _txt_search.wait_until(be.visible)
    _txt_search.send_keys(keyword)


@when("I enter {username} on username textbox")
def step_impl(context, username):
    _txt_username.wait_until(be.visible)
    _txt_username.send_keys(username)


@when("I enter {password} on password textbox")
def step_impl(context, password):
    _txt_password.wait_until(be.visible)
    _txt_password.send_keys(password)


@when("I click Log in button")
def step_impl(context):
    _btn_Login.wait_until(be.visible)
    _btn_Login.click()


@when("I search google with keyword as value below")
def step_impl(context):
    table_data = context.table

    for data in table_data:
        keyword = data.get('value')

    _txt_password.wait_until(be.visible)
    _txt_password.send_keys(keyword)


@then("Users are taken to Slide List page")
def step_impl(context):
    _link_slide_list.wait_until(be.visible)
    actual_result = _link_slide_list.get_text()
    expected_result = 'Slide List'
    assert actual_result == expected_result
