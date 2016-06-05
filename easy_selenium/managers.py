# -*- coding: utf-8 -*-

import functools
from contextlib import contextmanager
from easy_selenium import wrappers


@contextmanager
def webdriver(
        webdriver,
        window_size=None,
        script_timeout=10,
        page_load_timeout=50,
        implicity_wait_timeout=1):

    if not window_size:
        window_size = (1920, 1080)

    browser = webdriver()
    browser.set_window_size(*window_size)
    browser.implicitly_wait(implicity_wait_timeout)
    browser.set_page_load_timeout(page_load_timeout)
    browser.set_script_timeout(script_timeout)
    try:
        yield browser
    finally:
        browser.close()
        browser.quit()


firefox_webdriver = functools.partial(
    webdriver, webdriver=wrappers.FirefoxBrowser)

chrome_webdriver = functools.partial(
    webdriver, webdriver=wrappers.ChromeBrowser)
