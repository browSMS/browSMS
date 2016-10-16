'''

	For scraping some content from some damn HTML pages m8

'''

from lxml import html
import requests


def parsecontent(tree):

    #p = tree.xpath('//*[self::p or self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6]/text()')
    p = tree.xpath('//*/text()')
    p = [x.strip() for x in p if x.strip()]
    return p
    #print(type(p))
    #print(str(p))
    #for x in p:
        #print(x)
