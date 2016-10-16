"""
Retrieves the HTML from a webpage for processing.

Uses `parser.py` to parse salient data from the webpage.

Passes back the data to the messaging service for formatting and sending to the client.
"""
from lxml import html
from contents import parsecontent
import requests

def request():
	
	page = requests.get("http://deinosaur.github.io/cody-go-fish/")
	print(page.status_code)
	print(page.headers['content-type'])
	print(page.encoding)

	if (page.status_code == 200):
		tree = html.fromstring(page.content)
	print(type(tree))
	parsecontent(tree)


request()
