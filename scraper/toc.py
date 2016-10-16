'''
Returns the table of contents of the webpage

Contains:
menu: maps between text and url to go to, returns best image too
search<string query>: pass in this string into the search bar
show more: show more images or menus

'''

from lxml import html
import requests
import re

def menu(url):
    page = requests.get(url)

def search():
    page = requests.get("http://www.facebook.com")
    print(page.content)
    if (page.status_code == 200):
        print("hello")

def moreImages():
    pass

def moreMenus():
    pass