from bs4 import BeautifulSoup
import requests
import pprint


def getDepthHtml(ourLandsAbbr):
	# Create a variable with the URL to this tutorial
	url = 'http://www.ourlads.com/nfldepthcharts/depthchart/'+ourLandsAbbr
	# Scrape the HTML at the url
	r = requests.get(url)

	# Turn the HTML into a Beautiful Soup object
	soup = BeautifulSoup(r.text, 'html.parser')

	table = soup.find(class_='table table-bordered')

	for row in table.find_all('td'):
		try:
			if 'dt-sh' in row.attrs['class']:
				row.extract()
		except:
			pass

	return table
