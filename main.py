import requests
from bs4 import BeautifulSoup

url = "https://deepstatemap.live"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup.parserClass)
    #for element in soup.find_all('a'):
    #    print(element.text)
    #print(soup)
    print(soup.find('div', id='map'))
else:
    print("Error: Could not retrieve webpage")

