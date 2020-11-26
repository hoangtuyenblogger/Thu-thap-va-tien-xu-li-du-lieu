from newspaper import Article
from bs4 import BeautifulSoup
import requests
import sqlite3


def get_data(conn,url):

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")

        # get job about
        job_about = soup.find('ul', class_="list-unstyled fs-14 mb-0")

        # get job name
        job_name = job_about.find('h1', class_='fs-20 m-0').text

        # get company name
        company_name = job_about.find('a', class_="color-main fs-16").text.strip()

        #get location -> find all element li -> get li[2]
        all_li_element = job_about.findAll('li')
        location = all_li_element[2].text.replace("Địa điểm tuyển dụng: ","").strip()

        # get salary
        salary = job_about.find('span', class_="color-ed145b").text

        # get Occupations -< 'a' -> id = tv-tags color-main
        occupations = soup.findAll('a', class_="tv-tags color-main")
        occupation = ""
        for i in occupations:
            occupation += i.text + " "
            occupation.strip()

        # get ul class ="list-unstyled fs-14"
        div_job = soup.find('div', class_='tv-job-detail-more mt-30')
        ul = div_job.find('ul')
        li = ul.findAll('li')
        sex = str(li[0].text).replace("Yêu cầu giới tính","").strip()
        level = str(li[1].text).replace("Bằng cấp","").strip()
        ex = str(li[2].text).replace("Kinh nghiệm","").strip()
        lang = str(li[3].text).replace("Ngôn ngữ", "").strip()


        article = Article(url)
        article.download()
        article.parse()

        query = """
        INSERT INTO JOBS_DATA (
                          TITLE,
                          DESCRIPTION,
                          LINK,
                          JOB_NAME,
                          LOCATION,
                          COMPANY_NAME,
                          SALARY,
                          CONTENT,
                          OCCUPATIONS,
                      )
                      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """

        conn.execute(query,(article.title,article.meta_description,article.url,job_name,location,
                            company_name,salary,article.text,occupation)) # thêm dữ liệu craw vào db
        conn.commit()




        '''
        f_writer.writerow([article.title,article.meta_description,article.url,job_name,company_name,location,salary,article.text])
        print("article.title: ", article.title)
        print("article.meta_description:", article.meta_description)
        print("Link: ", article.url)
        print("Job name: ", job_name)
        print("Company name: ", company_name)
        print("Location: ",location)
        print("Salary: ",salary)
        print("article.text: ",article.text)
        '''

    except Exception as ex:
        print("Erro: ", ex)
        pass

def craw_from_links():
    conn = sqlite3.connect("data/DBTimviec.db")
    a = int(input("Bắt đầu từ : "))
    b = int(input("Đến : "))
    data = conn.execute("select * from LINKS_JOB WHERE ID BETWEEN ? AND ?", (a, b))

    for row in data:
        get_data(conn, row[1])
        print("Crawling . . . ", " id = ", a, row[1])
        a += 1
if __name__ == '__main__':
    print("haha")