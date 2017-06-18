## easy-selenium

[![PyPI version](https://badge.fury.io/py/easy-selenium.svg)](https://badge.fury.io/py/easy-selenium)

Selenium is a wonderful testing tool. This package aims to make easier and cleaner to write selenium scripts. However, in this package we assume that you are using XPATH always for the sake of simplicity.

### Why XPATH?

First, I would like to extract a piece of selenium's documentation:

> XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications. XPath extends beyond (as well as supporting) the simple methods of locating by id or name attributes, and opens up all sorts of new possibilities such as locating the third checkbox on the page.
> One of the main reasons for using XPath is when you don’t have a suitable id or name attribute for the element you wish to locate. 

Basically, the XPATH is easier when a website has few ids or classes in their HTML tags in addition to work for any XML structure.

### Example of some actions

##### Open popup

```python

from easy_selenium import wrappers

browser = wrappers.FirefoxBrowser()
browser.get('http://example.com/')

with browser.open_popup('//button[@id="open_popup"]'):
    do_something()

```

##### Finding elements and accessing attributes

```python
from easy_selenium import wrappers

browser = wrappers.FirefoxBrowser()
browser.get('http://example.com/')

title = browser.find_one('//h1[@id="title"]')
print(title.attr('text'))
# >> Text of title

for link in browser.find('//a'):
    print(link.attr('href'))
    # >> http://example.com/

```

##### Hide or Show elements

Sometimes you want a text of a div or span with style `hidden`, but when a element is hidden the selenium webdriver "can't see" the text. So, you need to show this element:

```python
from easy_selenium import wrappers
from easy_selenium import tools

browser = wrappers.FirefoxBrowser()
browser.get('http://example.com/')

# Use JQuery to show the element
hidden_div = browser.find_one('//div[@class="hidden"]')
tools.show_element(hidden_div)

# Use JQuery to hide the element
tools.hide_element(hidden_div)

```

### Installing

```bash

$ pip install easy-selenium

```
