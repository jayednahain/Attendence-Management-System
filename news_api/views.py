from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs



url_dhakatribune = 'https://www.dhakatribune.com/articles/latest-news/dhaka'
news_response_dhakatribune = requests.get(url_dhakatribune)
html_dhakatribune = news_response_dhakatribune.text
soup_div_dhakatribune = bs(html_dhakatribune,'html.parser')



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

   dicts = {}
   keys = range(len(values))

   for i in keys:
      dicts[i] = values[i]


   return render(request,'scarp_news.html',{"dicts":dicts})


def trebune_news(request):
   title_list = []
   #title_link_list = []
   body_list = []
   #image_link = []
   #title_list_frash = []
   #body_list_frash= []

   div_one = soup_div_dhakatribune.find('div', {'class': 'listing-page-news listing-page-info'})
   for div_two in div_one.find('div'):
      ## div_three=div_two.find('div',{'class':'col-sm-4'})
      h4_data = div_two.find('h4')
      title_list.append(h4_data)
      p_data = div_two.find('p')
      body_list.append(p_data)
      #img_link = div_two.find('img')
      #image_link.append(img_link)
      #title_link = div_two.find('a')
      #title_link_list.append(title_link)

   for x in title_list:
      if x == -1:
         title_list.remove(x)
   for x in title_list:
      if x == None:
         title_list.remove(x)

   title_list_frash = []
   for data in title_list:
      title_list_frash.append(data.string)
   dicts_title = {}
   keys = range(len(title_list_frash))
   for i in keys:
      dicts_title[i] = title_list_frash[i]




   for x in body_list:
      if x == -1:
         body_list.remove(x)

   for x in body_list:
      if x == None:
         body_list.remove(x)
   body_list_frash = []
   for data in body_list:
      body_list_frash.append(data.string)
   dicts_body = {}
   keys = range(len(body_list_frash))

   for i in keys:
      dicts_body[i] = body_list_frash[i]
   # print(dicts_body)






   #print(dicts_title)




   return render(request,'tribune_news.html',{'dict_title':dicts_title,'dict_body':dicts_body})



