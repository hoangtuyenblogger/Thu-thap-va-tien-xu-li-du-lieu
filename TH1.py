import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuoitrethudo.com.vn/xa-hoi")
soup = BeautifulSoup(response.content, "html.parser")

# lấy tất cả tiêu đề
titles = soup.findAll('h3', class_='article-title')
#lấy tất cả link
links = [link.find('a').attrs["href"] for link in titles]
#Lấy dữ liệu chi tiết từng bài
for link in links:
    news = requests.get(link)
    soup = BeautifulSoup(news.content, "html.parser")
    title = soup.find("h1", class_="bx-post-title").text # tiêu đề
    abstract = soup.find("div", class_="bx-desc f1 clearfix").text # mô tả
    body = soup.find("div", class_="__MB_CONTENT clearfix") # phần main
    content = body.findChildren("p", recursive=False)[0].text +      body.findChildren("p", recursive=False)[1].text
    image = body.find("img").attrs["src"]
    print("Tiêu đề: " + title)
    print("Mô tả: " + abstract)
    print("Nội dung: " + content)
    print("Ảnh minh họa: " + image)
    print("_________________________________________________________________________")
