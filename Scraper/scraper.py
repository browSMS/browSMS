from lxml import html
from lxml import etree
from contents import parsecontent
from toc import menu
##from login import getlogin
import requests

"""
Retrieves the HTML from a webpage for processing.

Uses:
contents.py for parsing the data of the webpage
toc.py for parsing the menu actions of the webpage
login.py for parsing possible login forms from the webpage
images.py for parsing the most relevant image from the webpage

Passes back an array of two elements:
0 -> string representing the data of the webpage
1 -> an array of tuples representing possible menu actions
2 -> an optional relevant image
"""
def navigate(url):
	
	page = requests.get(url)
	#print(page.status_code)
	#print(page.headers['content-type'])
	#print(page.encoding)

	if (page.status_code == 200):
		tree = html.fromstring(page.content)

		# Strip head from tree
		for head in tree.xpath('//head'):
			head.getparent().remove(head)

		##print(etree.tostring(tree, pretty_print=True))

		# Generate table of contents
		parsed_menu = menu(tree, url)

		# Generate login information (deprecated)
		##parsed_menu.append(getlogin(tree))

		# Generate contents from cleaned tree
		parsed_webpage_data = parsecontent(tree)

		if (len(parsed_webpage_data) > 1200):
			parsed_webpage_data = parsed_webpage_data[:1197] + '...'

		# Find the most important image
		parsed_image = None #getimage(tree)

		return [parsed_webpage_data, parsed_menu, parsed_image];

		#DEBUG
		##return [
		##	['Alec Baldwin is a pal', 'he is a person who acts; an actor', 'he is a pal'],
		##	[('About', 'http://www.alecbaldwin.com/about'), ('30 Rock', 'http://www.alecbaldwin.com/category/media'), ('Ideas', 'http://www.alecbaldwin.com/category/ideas')],
		##	'http://www.alecbaldwin.com/wp-content/uploads/2011/05/alex-baldwin-headshot.png'
		##]

	else:
		return page.status_code

if (__name__ == '__main__'):
	navigate('http://www.cs.washington.edu/143')
