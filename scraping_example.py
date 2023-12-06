import requests 
from bs4 import BeautifulSoup as bs 

url = 'https://www.livehealthily.com/health-library#symptoms'

response = requests.get(url)

if response.status_code == 200:
    soup = bs(response.text, 'html.parser')
    li_tags = soup.find_all('div')
    print(li_tags)