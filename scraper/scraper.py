from lxml import html
from lxml import etree
from contents import parsecontent
from toc import getmenu
from login import getlogin
import requests

"""
Retrieves the HTML from a webpage for processing.

Uses:
contents.py for parsing the data of the webpage
toc.py for parsing the menu actions of the webpage
login.py for parsing possible login forms from the webpage
images.py for parsing the most relevant image from the webpage

Passes back an array of two elements:
0 -> a string representing the data of the webpage
1 -> an array of tuples representing possible menu actions
2 -> an optional relevant image
"""
def navigate(url):
	
	page = requests.get(url)
	print(page.status_code)
	print(page.headers['content-type'])
	print(page.encoding)

	if (page.status_code == 200):
		tree = html.fromstring(page.content)

		# Strip head from tree
		for head in tree.xpath('//head'):
			head.getparent().remove(head)

		print(etree.tostring(tree, pretty_print=True))

		# Generate table of contents
		menu = getmenu(tree)

		# Generate login information
		menu.append(getlogin(tree))

		# Generate contents from cleaned tree
		webpageData = parsecontent(tree)

		# Find the most important image
		image = getimage(tree)

		return [webpageData, menu, image];

	else:
		return page.status_code

<<<<<<< HEAD
	navigate(2, 'http://deinosaur.github.io/cody-go-fish/')

getSessionData(2)
=======
navigate('www.cs.washington.edu/332')
>>>>>>> aed71bb30ae4eabf7b41e4bfac60135e543b3ff4
