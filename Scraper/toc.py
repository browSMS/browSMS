'''
Returns the table of contents of the webpage

Contains:
menu: maps between text and url to go to, returns best image too
search<string query>: pass in this string into the search bar
show more: show more images or menus

'''


from urlparse import urlparse
from lxml import html
import pprint
import requests
import re

def menu(tree, url):
    possibleMenus = [
        tree.find_class('navbar'),
        tree.find_class('nav'),
        tree.find_class('menubar'),
        tree.find_class('menu'),
        tree.find_class('menu_item'),
        tree.find_class('nav-flyout__container'),
        tree.find_class('nav-menu-links')
    ]

    result = []

    for possibleMenu in possibleMenus:
        if len(possibleMenu) != 0:
            for menuRoot in possibleMenu:
                for child in menuRoot.iterchildren():
                    linkTarget = child.get('href')
                    if (linkTarget != None):
                        if (linkTarget.startswith('http') or linkTarget.startswith('www')):
                            result.append((child.text_content(), linkTarget))
                        else:
                            result.append((child.text_content(), url + linkTarget))
    print(result)
    return result


def search():
    page = requests.get("http://www.facebook.com")
    print(page.content)
    if (page.status_code == 200):
        print("hello")

def moreImages():
    pass

def moreMenus():
    pass

def getimage(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain + 'favicon.ico'