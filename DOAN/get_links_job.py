from bs4 import BeautifulSoup
import requests
import csv
import sqlite3

f = open('link.csv', 'a+')
f_writer = csv.writer(f,lineterminator='\n')


def get_links_job(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    list_new_job = soup.findAll('div', class_="field-thumbnail mr-12")
    link_jobs = [link.find('a').attrs['href'] for link in list_new_job]

    conn = sqlite3.connect("data/DBTimviec.db")
    query = """
    INSERT INTO LINKS_JOB(LINK) VALUES (?)
    """

    for link in link_jobs:
        #f_writer.writerow([link.strip()]) # add link to csv
        conn.execute(query,(link,))
        conn.commit()
        print("added to database ",link)

def get_links_job_from_range_page():
    a = int(input("Lấy link bắt đầu từ phân trang thứ : "))
    b = int(input("Đến phân trang thứ :"))
    link = "https://timviec.com.vn/tim-viec-lam?order_by=renew_int&page="
    for i in range(a,b+1,1):
        url = link + str(i)
        get_links_job(url)

if __name__ == '__main__':
    a = int(input("Lấy link bắt đầu từ phân trang thứ : "))
    b = int(input("Đến phân trang thứ :"))
    link = "https://timviec.com.vn/tim-viec-lam?order_by=renew_int&page="
    for i in range(a,b+1,1):
        url = link + str(i)
        get_links_job(url)

