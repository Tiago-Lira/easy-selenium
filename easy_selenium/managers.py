from __future__ import absolute_import, division, print_function, unicode_literals  # noqa

import functools
from contextlib import contextmanager

from easy_selenium import wrappers
from easy_selenium.globals import browser_context, context


@contextmanager
def webdriver(
        webdriver,
        window_size=None,
        **kwargs):

    if not window_size:
        window_size = (1920, 1080)

    browser = webdriver(**kwargs)
    browser.set_window_size(*window_size)
    with browser_context():
        try:
            context.browser = browser
            yield browser
        finally:
            browser.close()
            browser.quit()

firefox_webdriver = functools.partial(
    webdriver, webdriver=wrappers.FirefoxBrowser)

chrome_webdriver = functools.partial(
    webdriver, webdriver=wrappers.ChromeBrowser)
