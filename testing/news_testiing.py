import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.dhakatribune.com/articles/latest-news/dhaka'
news_response = requests.get(url)
html = news_response.text

soup_div = bs(html,'html.parser')
