"""
Retrieves the HTML from a webpage for processing.

Uses `parser.py` to parse salient data from the webpage.

Passes back the data to the messaging service for formatting and sending to the client.
"""
from lxml import html
from lxml import etree
from contents import parsecontent
import requests

def navigate(uid, url):
	
	page = requests.get("http://deinosaur.github.io/cody-go-fish/")
	print(page.status_code)
	print(page.headers['content-type'])
	print(page.encoding)

	if (page.status_code == 200):
		tree = html.fromstring(page.content)

		# Strip head from tree
		for head in tree.xpath('//head'):
			head.getparent().remove(head)

		print(etree.tostring(tree, pretty_print=True))

		# TODO: call toc

		# Generate contents from cleaned tree
		parsecontent(tree)

def getSessionData(uid):
	#TODO: gets data about the settions from the database, only used internally for navigate

	navigate(2, 'http://deinosaur.github.io/cody-go-fish/')

getSessionData(2)
