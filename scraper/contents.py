'''

	For scraping some content from some damn HTML pages m8

'''

from lxml import html
import requests

page = requests.get("http://deinosaur.github.io/cody-go-fish/")
tree = html.fromstring(page.content)

str(tree)
print(tree)

p = tree.xpath('//p/text()');
print(p)
