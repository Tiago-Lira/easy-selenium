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

    def find_one(self, xpath):
        el = self.find_element_by_xpath(xpath)
        return self.__class__(el._parent, el._id, w3c=el._w3c)

    def find(self, xpath):
        for el in self.find_elements_by_xpath(xpath):
            yield self.__class__(el._parent, el._id, w3c=el._w3c)

    def write(self, value, verify_read_only=False, clear_before=True):
        if not verify_read_only:
            if clear_before:
                self.clear()
            self.send_keys(value)
            return True

        elif not self.attr('readonly'):
            if clear_before:
                self.clear()
            self.send_keys(value)
            return True
        return False

    def attr(self, key):
        return self.get_attribute(key)
