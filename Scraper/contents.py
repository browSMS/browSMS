'''
Scrape content from html page
'''

from lxml import html
import re

def parsecontent(tree):
    result = ' '.join(tree.text_content().strip().split())
    links = []
    for href in tree.xpath('//a/@href'):
        a = href.getparent()
        if a.text:
            links.append((a.text.strip(), str(href)))
            a.text = ' {' + a.text.strip() + '} '

    result = tree.text_content()
    result = re.sub(r'[^\x00-\x7F]+', '', result)
    result = ' '.join(result.strip().split())
    # i = 0
    # while i < len(result) - 1:
    #     if result[i].islower() and result[i + 1].isupper():
    #         result = result[:i + 1] + '. ' + result[i + 1:]
    #         i += 2
    #     i += 1
    return links, result
