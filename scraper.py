import requests
from bs4 import BeautifulSoup
def Intake():
	URL = 'http://localhost:8080/it.html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='it_intake').get_text()
	## results = soup.find(id="",{})
	return results

def Itprof():
	URL = 'http://localhost:8080/it.html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='itprof').get_text()
	## results = soup.find(id="",{})
	return results

def Fees1():
	URL = 'http://localhost:8080/sakec_web1 (1).html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='fees1').get_text()
	## results = soup.find(id="",{})
	return results

def Fees2():
	URL = 'http://localhost:8080/sakec_web1 (1).html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='fees2').get_text()
	## results = soup.find(id="",{})
	return results

def Fees3():
	URL = 'http://localhost:8080/sakec_web1 (1).html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='fees3').get_text()
	## results = soup.find(id="",{})
	return results

def Fees4():
	URL = 'http://localhost:8080/sakec_web1 (1).html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='fees4').get_text()
	## results = soup.find(id="",{})
	return results

def Register():
	URL = 'http://localhost:8080/sakec_web1 (1).html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='register').get_text()
	## results = soup.find(id="",{})
	return results

def Contact():
	URL = 'http://localhost:8080/sakec_web1 (1).html'
	page = requests.get(URL)


	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='contact').get_text()
	## results = soup.find(id="",{})
	return results









