import crawler_post
import get_links_job
import pandas
import csv
import sqlite3
import numpy
import re
import matplotlib
from main import *
import nltk
from nltk import *
#from matplotlib import pyplot as bieudo
import spacy
from main import *

def thong_ke_nganh_nghe(nganh_nghe):
    # xử lí, tách ngành nghề bỏ vào list, set
    list_nganh_nghe = []
    for nghe in nganh_nghe:
        # bỏ dấu '/'
        nghe = str(nghe).replace('/', "") # -> nghe =  "Hành chính  Thư ký Hành chính văn phòng Bất động sản"
        a = re.split(r" (?=[A-Z])",nghe) # a = ['Trợ lý', 'Hành chính văn phòng', 'Bất động sản'] dùng Regex
        for i in a:
            list_nganh_nghe.append(i.replace('nhân viên kinh doanh',"Kinh doanh").replace("nhân viên tư vấn","Tư vấn").replace("Kinh doanh Kinh doanh bất động sản","Kinh doanh").replace("Kinh doanh  bất động sản","Bất động sản").replace("Kinh doanh Kinh doanh","Kinh doanh").strip()) # thêm từng ngành nghề vào list

    set_list_nganh_nghe = set(list_nganh_nghe) # loại bỏ các nghề trùng nhau
    for nghe in set_list_nganh_nghe:
        print(nghe)
    print("----------------------------------------------------------------")
    print('Thống kê số lượng bài tuyển dụng theo nghành nghề: ( hơn 100 bài)')
    for i in set_list_nganh_nghe:
        count = list_nganh_nghe.count(i)
        if count > 100:
            print(str(i).strip(), ":", count)
    print("-------------------------Thống kê ngành nghề--------------------------------")
    print("Có tổng số ngành nghề: ", len(set_list_nganh_nghe))

    fdist_nganh_nghe = FreqDist(list_nganh_nghe) #tuần suất xuất hiện
    fdist_nganh_nghe.plot(10) # vẽ biểu đồ




if __name__ == '__main__':
    thong_ke_nganh_nghe(nganh_nghe)