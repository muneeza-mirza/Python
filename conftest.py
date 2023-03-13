import json

import pytest
from pytest import fixture
from selenium import webdriver

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome('../chromedriver/chromedriver.exe')
    yield browser


@fixture(scope='session')
def session_func():
    print("session")

@fixture(scope='module')
def mod_func():
    print("module")

@fixture(scope='class')
def play_with_nos(request):
    print("class")
    request.cls.text= 'a'


@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    drvr=driver()
    yield drvr
    drvr.quit()