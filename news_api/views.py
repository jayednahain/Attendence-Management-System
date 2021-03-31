from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com'
news_response = requests.get(url)
html = news_response.text

soup_div = bs(html,'html.parser')



def scarp_news(request):
   filter_by = {
      'class': 'text'
      # class that contains 'text' value
   }
   filter_by = {
      'class': 'text'
   }
   values = []



   for tag_Data in soup_div.findAll('span', filter_by):
      data = tag_Data.string
      values.append(data.replace('“', '').replace('”', ''))

   send_data = {}



   return render(request,'scarp_news.html',{})
