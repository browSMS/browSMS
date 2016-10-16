'''

	For scraping some content from some damn HTML pages m8

'''

from lxml import html
import requests


def parsecontent(tree):

    p = tree.xpath('//p/text()')
    print(type(p))
    for item in p:
        print(str(item).strip())
