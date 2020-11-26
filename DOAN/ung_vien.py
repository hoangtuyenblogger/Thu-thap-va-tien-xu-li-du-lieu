from bs4 import BeautifulSoup
import requests
import sqlite3
from nltk import FreqDist


def get_ung_vien(conn,url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")

        ten_ung_vien = []
        ten_cv = []
        kinh_nghiem = []
        dia_diem = []

        # lay ten ung vien
        ung_vien_element = soup.findAll('p', class_="fw-400 mb-0 fs-14")

        # lay ten cong viec ung tuyen
        job_name_element = soup.findAll('span', class_='job-name')

        # lat kinh nghiem
        kinh_nghiem_element = soup.findAll('li', class_="g-width-30x")

        # lay dia diem lam viec
        locations = soup.findAll('li', class_="g-width-40x")
        for i in range(len(ung_vien_element)):
            ten_ung_vien.append(str(ung_vien_element[i].text).strip())
            ten_cv.append(str(job_name_element[i].text).strip())
            kinh_nghiem.append(str(kinh_nghiem_element[i].text).replace("Kinh nghiệm:","").strip())
            dia_diem.append(str(locations[i].text).replace("Địa điểm:", "").strip())
        #print(ten_ung_vien)
        #print(dia_diem)
        #print(ten_cv)
        #print(kinh_nghiem)

        query = """
        INSERT INTO EMPLOYER(NAME,JOB_NAME,LOCATION,EX) VALUES(?,?,?,?) 
        """
        for i in range(len(ten_ung_vien)):
            conn.execute(query,(str(ung_vien_element[i].text).strip(),
                                str(job_name_element[i].text).strip(),
                                str(locations[i].text).replace("Địa điểm:", "").strip(),
                                str(kinh_nghiem_element[i].text).replace("Kinh nghiệm:","").strip()))
            conn.commit()
            print("Đã thêm ", " . . .",str(ung_vien_element[i].text).strip())

    except Exception as ex:
        print("Erro: ", ex)
        pass
def get_ung_vien_theo_phan_trang():
    conn = sqlite3.connect("data/DBTimviec.db")
    link = "https://timviec.com.vn/ung-vien?page"

    a = int(input("Bắt đầu craw từ phân trang thứ: "))
    b= int(input("Đến phân trang thứ: "))
    for i in range(a,b+1):
        url = link + str(i)
        get_ung_vien(conn,url)


def thong_ke_nganh_nghe_ung_vien(nganh_nghe):
    from matplotlib import pyplot as bieudo
    # xử lí, tách ngành nghề bỏ vào list, set
    list_nganh_nghe = []
    for nghe in nganh_nghe:
        list_nganh_nghe.append(nghe.replace('nhân viên kinh doanh',"Kinh doanh").replace("nhân viên tư vấn","Tư vấn").replace("Kinh doanh Kinh doanh bất động sản","Kinh doanh").replace("Kinh doanh  bất động sản","Bất động sản").replace("Kinh doanh Kinh doanh","Kinh doanh").strip()) # thêm từng ngành nghề vào list

    set_list_nganh_nghe = set(list_nganh_nghe) # loại bỏ các nghề trùng nhau
    for nghe in set_list_nganh_nghe:
        print(nghe)
    print("----------------------------------------------------------------")
    print('Thống kê số lượng bài tuyển dụng theo nghành nghề: ')
    for i in set_list_nganh_nghe:
        count = list_nganh_nghe.count(i)
        if count > 100:
            print(str(i).strip(), ":", count)

    print("-------------------------Thống kê ngành nghề--------------------------------")
    print("Có tổng số ngành nghề: ", len(set_list_nganh_nghe))



    fdist_nganh_nghe = FreqDist(list_nganh_nghe) #tuần suất xuất hiện
    fdist_nganh_nghe.plot(20) # vẽ biểu đồ
if __name__ == '__main__':
    get_ung_vien_theo_phan_trang()
    print("Đã xong. . . .")