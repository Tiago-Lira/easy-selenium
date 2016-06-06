
from __future__ import absolute_import, division, print_function, unicode_literals  # noqa

try:
    import urlparse as parse
except ImportError:
    from urllib import parse

from selenium.webdriver.support import ui
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as ec

from easy_selenium.webelement import Element
from easy_selenium.webelement import popup


class Browser(object):

    def find_one(self, xpath):
        element = self.find_element_by_xpath(xpath)
        return Element(self, element)

    def find(self, xpath):
        for el in self.find_elements_by_xpath(xpath):
            yield Element(self, el)

    def set_cookies(self, cookies, domain=None):
        for key, value in cookies.items():
            cookie = {}
            cookie['name'] = key
            cookie['value'] = value
            cookie['domain'] = domain or self.get_domain()
            self.add_cookie(cookie)

    def get_domain(self):
        parsed = parse.urlparse(self.current_url)
        return parsed.hostname

    def write(self, value, xpath=None, element=None,
              verify_read_only=False, clear_before=True):
        if xpath:
            element = self.find(xpath)
        return element.write(
            value, verify_read_only=verify_read_only,
            clear_before=clear_before)

    def wait_for_element(self, xpath, timeout=10):
        el = ui.WebDriverWait(self._driver, timeout).until(
            ec.presence_of_element_located((by.By.XPATH, xpath))
        )
        return Element(self, el)

    def open_popup(self, xpath=None, element=None, timeout=10):
        if xpath:
            element = self.find(xpath)
        return popup(self, element, timeout=timeout)

    def click(self, xpath):
        element = self.find(xpath)
        return element.click()
