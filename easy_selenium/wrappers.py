# -*- coding: utf-8 -*-

from selenium import webdriver
from easy_selenium.webdriver import Browser


class FirefoxBrowser(Browser, webdriver.Firefox):
    pass


class ChromeBrowser(Browser, webdriver.Chrome):
    pass
