from behave import given, when, then

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


# @given(u'I am on the Fibers Digitalization Platform login page')
# def step_impl(context):
#   driver_path = ChromeDriverManager().install()
#   driver = webdriver.Chrome(driver_path)
#   driver.get("http://10.10.10.7:8081/")
# driver.close()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# context.driver.get("")
# assert "Log in" in context.driver.page_source

# @when(u'I enter username {username} and the user\'s {correctness} password')
# def step_impl(context, username, correctness):
#   userName = context.driver.find_element_by_xpath("//input[@formcontrolname='userName']")
#   userName.clear()
#   userName.send_keys(username)
#   password = context.driver.find_element_by_xpath("//input[@formcontrolname='password']")
#   password.clear()
#   sentPwd = "fakePwd"
#   if correctness == "correct":
#     if username == "SGS-admin":
#       sentPwd = "sgs123"
#     elif username == "labworld-admin":
#       sentPwd = "labworld123"
#   password.send_keys(sentPwd)
#   password.send_keys(Keys.RETURN)
#   time.sleep(0.5)

# @when(u'I click logout')
# def step_impl(context):
#   logOut = context.driver.find_element_by_xpath('//button[text()="Log out"]')
#   logOut.click()


# @then(u'I am on the page {page}')
# def step_impl(context,page):
#   if "Slide manager" in page:
#     assert "Slide List" in context.driver.page_source
#   elif "Login fail page" in page:
#     assert "Incorrect username or password" in context.driver.page_source
#   elif "MainPage" in page:
#     assert "Log in" in context.driver.page_source
#     assert "Incorrect username or password" not in context.driver.page_source
#   else:
#     assert 1 == 2, "Class not implemented"
