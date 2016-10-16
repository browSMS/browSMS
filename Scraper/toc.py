'''
Returns the table of contents of the webpage

Contains:
menu: maps between text and url to go to, returns best image too
search<string query>: pass in this string into the search bar
show more: show more images or menus

'''

from lxml import html
import pprint
import requests
import re

def menu(tree):
    possibleMenus = [
        tree.find_class('navbar'),
        tree.find_class('nav'),
        tree.find_class('menubar'),
        tree.find_class('menu'),
        tree.find_class('menu_item'),
        tree.find_class('nav-flyout__container')
    ]

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(possibleMenus)

    for possibleMenu in possibleMenus:
        if len(possibleMenu) != 0:
            print('hey')

    print(possibleMenus)

    return possibleMenus


def search():
    page = requests.get("http://www.facebook.com")
    print(page.content)
    if (page.status_code == 200):
        print("hello")

def moreImages():
    pass

def moreMenus():
    pass