import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []



