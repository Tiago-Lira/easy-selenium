
from __future__ import absolute_import, division, print_function, unicode_literals  # noqa

from easy_selenium.managers import context


def get_browser():
    try:
        return context.browser
    except AttributeError:
        raise RuntimeError('Working outside of browser context.')


def show_element(element, browser=None):
    browser = browser or get_browser()
    browser.execute_script("""
        $(arguments[0]).show();
    """, element)


def hide_element(element, browser=None):
    browser = browser or get_browser()
    browser.execute_script("""
        $(arguments[0]).hide();
    """, element)
