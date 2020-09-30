import time
import re
import csv
from bs4 import BeautifulSoup

from urllib import request

def fetch_url(url):
  opener = request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0')]
  request.install_opener(opener)
  html_string = request.urlopen(url).read()
  return html_string.decode()
import time
import json

# some JSON:
film_list = []

films_url = fetch_url('https://www.imdb.com/list/ls055386972/')
#print(films_url)
films_soup = BeautifulSoup(films_url)

#films_html = films_url(films_url + f'?page={i}')
film_info_inner = films_soup.find_all('div', {'class' : 'lister list detail sub-list'})
titlesList = []
directorsList = []
for film_list in film_info_inner:
  film_info_list = films_soup.find_all('div', {'class': 'lister-item mode-detail'})
  film_director = films_soup.find_all('p', {'class': 'text-muted text-small'})

  z = 1
  for i in range(49):
    director = film_director[z].text.split('\n')[2]
    z = z+3
    directorsList.append(director)




  for item in film_info_list:
    title = item.text.split('\n')
    titleList = []
    for word in title:
      if len(word) > 5:
        titleList.append(word)
    titlesList.append(titleList[0:3])

with open('filmy', 'w', newline='') as myfile:
  for z in range(49):
    titlesList[z].append(directorsList[z])
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(titlesList[z])




