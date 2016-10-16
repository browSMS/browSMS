'''

craping some content from some damn HTML pages m8

'''

from lxml import html
import requests
import re


def parsecontent(tree):

    #p = tree.xpath('//*[self::p or self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6]/text()')
    p = tree.xpath('//*/text()')
    p = ''.join(p)
    p = re.sub(r'\n\s+\n\s+\n\s+', '\n', p)
    print(type(p))
    print(p)
    return p

