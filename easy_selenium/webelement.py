
from __future__ import absolute_import, division, print_function, unicode_literals  # noqa

import time
from contextlib import contextmanager

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


@contextmanager
def popup(browser, element, timeout=10):
    initial_window = browser.current_window_handle
    initial_windows = browser.window_handles
    time_elapsed = 0

    # Click to open the poup
    element.click()
    new_window = None

    while not new_window:
        new_window = [x for x in browser.window_handles
                      if x not in initial_windows]
        if not new_window:
            time.sleep(2)
            time_elapsed += 2
            if time_elapsed > timeout:
                raise exceptions.TimeoutException(
                    'Popup doesnt open in specified time')

    browser.switch_to_window(new_window)
    yield browser

    # Closes the new window
    if new_window in browser.window_handles:
        browser.switch_to_window(new_window)
        browser.close()

    # Back to initial window
    browser.switch_to_window(initial_window)


class Element(WebElement):

    def __init__(self, browser, element):
        self.browser = browser
        self.element = element
        self._parent = element._parent
        self._id = element._id
        self._w3c = element._w3c

    def find(self, xpath, many=False):
        cls = self.__class__
        if many:
            return [
                cls(self.browser, x) for x in
                self.element.find_elements_by_xpath(xpath)]
        else:
            el = self.element.find_element_by_xpath(xpath)
            return cls(self.browser, el)

    def write(self, value, verify_read_only=False, clear_before=True):
        if not verify_read_only:
            if clear_before:
                self.element.clear()
            self.element.send_keys(value)
            return True

        elif not self.attr('readonly'):
            if clear_before:
                self.element.clear()
            self.element.send_keys(value)
            return True

        return False

    def attr(self, key):
        return self.element.get_attribute(key)
