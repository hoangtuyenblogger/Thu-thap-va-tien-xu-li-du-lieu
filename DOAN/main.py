from thong_ke_dia_diem_tuyen_dung import *
from thong_ke_nganh_nghe import *
from Stopword import loai_bo_stopword, loai_bo_stopword_trong_danhsach
from get_links_job import  *
from crawler_post import *
from ung_vien import *
import bow_tf_idf
from Search import *
import sqlite3


conn = sqlite3.connect("data/DBTimviec.db")
query = "SELECT *  FROM JOBS_DATA"
data = conn.execute(query).fetchall()
tieude = []
mota = []
link = []
ten_cv = []
nganh_nghe = []
dia_diem = []
# -------------Load dữ liệu tuyển dụng--------------------- #
for row in data:
    tieude.append(row[1])
    mota.append(row[2])
    link.append([row[3]])
    ten_cv.append(row[4])
    nganh_nghe.append(row[5])
    dia_diem.append(row[6])
# ------------------load dữ liệu ứng viên-------------------- #
data_ungvien = conn.execute("SELECT * FROM EMPLOYER")
ten_ung_vien = []
nganh_nghe_ung_tuyen = []
dia_diem_ung_tuyen = []
kinh_nghiem = []
for row in data_ungvien:
    ten_ung_vien.append(row[1])
    nganh_nghe_ung_tuyen.append(row[2])
    dia_diem_ung_tuyen.append(row[3])
    kinh_nghiem.append(row[4])






'''
data = pandas.read_csv('data.csv')  #
print('----------------------------------------')
tieude = data['TITLE']
mota = data['DESCRIPTION']
link = data['LINK']
ten_cv = data['JOB_NAME']
nganh_nghe = data['OCCUPATIONS']
dia_diem = data['LOCATION']
ten_cty = data['COMPANY_NAME']
luong = data['SALARY']'''
'''data_ungvien = pandas.read_csv('ung_vien.csv')
ten_ung_vien = data_ungvien['NAME']
nganh_nghe_ung_tuyen = data_ungvien['JOB_NAME']
dia_diem_ung_tuyen = data_ungvien['LOCATION']
kinh_nghiem = data_ungvien['EX']'''

# ---------------------------------------------------------- #

def menu():
    try:
        while True:
            try:

                print("""
                        |-------------------------------------------------------------------------------|   
                        |   1.Thu thập link tuyển dụng                                                  |
                        |   2.Thu thập thông tin tuyển dụng(Tiêu đề, mô tả, vị trí tuyển dụng, . . .)   |
                        |   3.Thu thập thông tin ứng viên(Tên, bằng cấp, địa chỉ, . . )                 |
                        |   --------------------------------------------------------------------------- |
                        |   4.Loại bỏ Stopword                                                          |
                        |   5.Thống kế bao nhiêu ngành nghề đang tuyển dụng(Nhà tuyển dụng)             |
                        |   6.Thống kê địa điểm tuyển dụng                                              |
                        |   7.Thống kê bao nhiêu ngành nghề đang cần việc làm(Ứng viên)                 |                                              
                        |   8.Chuyển thông tin về dạng số tf-idf                                        |
                        |   9. Tìm kiếm thông tin                                                       |
                        |   --------------------------------------------------------------------------- |
                        |   0.Thoát                                                                     |
                        |------------------------------------------------------------------------------ |
                        """)
                option = int(input("Chọn chức năng: "))
                if option == 1:
                    get_links_job_from_range_page()
                elif option == 2:
                    craw_from_links()
                elif option == 3:
                    get_ung_vien_theo_phan_trang()
                elif option == 4:
                    print("""
                Loại bỏ stopword trong:
                1. tieude
                2. mota
                3. Ví dụ loại bỏ stopword""")
                    a = int(input("Chọn: "))
                    if a == 1:
                        print("Tiêu đề sau khi loại bỏ stopword: ")
                        for i in loai_bo_stopword_trong_danhsach(tieude):
                            print(i)
                    elif a == 2:
                        print("Mô tả sau khi loại bỏ stopword: ")
                        for i in loai_bo_stopword_trong_danhsach(mota):
                            print(i)
                    else:
                        sentence = input("Nhập vào 1 câu: ")
                        print("------------------ Câu đã nhập: ",sentence)
                        print("------------------ Câu sau khi loại bỏ stopword: ",loai_bo_stopword(sentence))
                elif option == 5:
                    thong_ke_nganh_nghe(nganh_nghe)
                elif option == 6:
                    thong_ke_dia_diem_tuyen_dung(dia_diem)
                elif option == 7:
                    thong_ke_nganh_nghe_ung_vien(nganh_nghe_ung_tuyen)
                elif option == 8:
                    bow_tf_idf.main()
                elif option == 9:
                    Search()
                else:
                    print("Đã thoát")
                    break
                    pass
            except Exception as erro:
                print("Hãy chọn đúng chức năng!")
                print(erro)
    except Exception as erro:
        print(erro)



if __name__ == '__main__':
    menu()




