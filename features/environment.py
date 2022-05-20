from behave.runner import Context
from selenium import webdriver
from features.page_object_models.index_page import IndexPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("F:/Revature_jd/chromedriver_win32/chromedriver.exe")
    context.index_page = IndexPage(context.driver)


def after_all(context):
    context.driver.quit()

