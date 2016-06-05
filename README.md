## easy-selenium

Selenium is a wonderful tool to testing, but some actions could be simplified.
Actions like open multiple popups and the name of certain methods would be much simplier using this package.
However, in this package we assume that you are using XPATH always for selecting the elements on the document.

### Why XPATH?

First, I would like to extract a text documentation of selenium library:

> XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications. XPath extends beyond (as well as supporting) the simple methods of locating by id or name attributes, and opens up all sorts of new possibilities such as locating the third checkbox on the page.
> One of the main reasons for using XPath is when you don’t have a suitable id or name attribute for the element you wish to locate. 

Basically, the XPATH is more easier when a website has few ids or classes in their HTML tags, in addition to work for any XML structure.

### Example of some actions

##### Open popup

```python

from easy_selenium import wrappers

browser = wrappers.FirefoxBrowser()
with browser.open_popup('//button[@id="open_popup"]'):
    do_something()

```

##### Finding elements and accessing attributes

```python
from easy_selenium import wrappers

browser = wrappers.FirefoxBrowser()
title = browser.find('//h1[@id="title"]')
print(title.attr('text'))
# >> Text of title

links = browser.find('//a', many=True)
for link in links:
    print(link.attr('href'))
    # >> http://example.com/

```


### Installing

```bash

$ pip install easy-selenium

```
