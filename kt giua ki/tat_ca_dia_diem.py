import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuyencongchuc.vn/")
soup = BeautifulSoup(response.content, "html.parser")


All_location = soup.findAll('div', id="location") # lấy tất cả địa điểm
#locations = [location.findAll('a') for location in All_location]
print('tất cả Địa điểm: ', All_location)


for i in All_location:
    location = i.find('a').text
    print('Địa điểm: ', location)
    print('------------------------------------------')

