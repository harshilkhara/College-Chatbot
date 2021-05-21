import requests
from bs4 import BeautifulSoup
def Intake():
	URL = 'https://www.shahandanchor.com/it'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(text='120')
	return results

