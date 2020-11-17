import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuyencongchuc.vn/")
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.findAll('div', id="titlo") # lấy tất cả tiêu đề bài báo
print('tiitle:', titles)
links = [link.find('a').attrs["href"] for link in titles] # lấy tất cả link từng bài báo ở trong titles

##############################################################################
All_location = soup.findAll('div', id="location") # lấy tất cả địa điểm
#locations = [location.findAll('a').attrs['href'] for location in All_location]
print('tất cả Địa điểm: ', All_location)


location = [i.find('a').text for i in All_location]
for i in location:
    print(i)
################################################################################


for link in links:
    news = requests.get(link) # request từng bài báo
    soup = BeautifulSoup(news.content, "html.parser") # tạo soup cho bài báo
    title = soup.find("h2", class_="title").text # lấy tiêu đề
    cre = soup.find('a').attrs["href"]
    #location_job = location.find('a').text
    print('Link bài báo: ',link)
    print('Tiêu đề: ', title)
    #print('Địa điểm: ',location_job)
    print('Nguồn tin: ', cre)
    print('------------------------------------------')


