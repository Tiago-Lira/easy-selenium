
from __future__ import absolute_import, division, print_function, unicode_literals  # noqa

from selenium import webdriver
from easy_selenium.webdriver import Browser


class FirefoxBrowser(Browser, webdriver.Firefox):
    pass


class ChromeBrowser(Browser, webdriver.Chrome):
    pass
