import requests
from bs4 import BeautifulSoup
def scrape_data(url):
     response = requests.get(url)
     soup = BeautifulSoup(response.text, 'html.parser')

     return soup


print(scrape_data('https://medium.com/@Evenword/20-python-scripts-with-code-to-automate-your-work-faedbf0231cc'))