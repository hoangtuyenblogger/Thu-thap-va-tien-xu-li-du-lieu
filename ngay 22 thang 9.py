import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.youtube.com/watch?v=b_NN_I5XV2c&ab_channel=Ph%E1%BA%A1mHuyHo%C3%A0ng")
soup = BeautifulSoup(response.content, "html.parser")

# lấy tất cả tiêu đề
titles = soup.findAll('h3', class_='article-title')
#lấy tất cả link

print(soup)