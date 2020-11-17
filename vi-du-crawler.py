import requests
from bs4 import BeautifulSoup


new = requests.get('https://tuoitre.vn/phap-luat.htm')
soup = BeautifulSoup(new.content, "html.parser")

titles = soup.findAll('h3', class_="title-news")
title = [i.find('a').attrs['title'] for i in titles]
for i in title:
    print('Tiêu đề :',i)


links = [i.find('a').attrs['href'] for i in titles]
for i in links:
    print('https://tuoitre.vn' + i)