from main import *
from nltk import *

def thong_ke_dia_diem_tuyen_dung(dia_diem):
    list_dia_diem = []
    for i in dia_diem:
        locations = str(i).strip().split(', ')### "Hồ Chí Minh, Bình Dương" -> "Hồ Chí Minh", "Bình Dương"
        for location in locations:
            list_dia_diem.append(location)
    set_dia_diem = set(list_dia_diem)
    print("---------------Thống kê địa điểm tuyển dụng---------------")
    for i in set_dia_diem:
        count = list_dia_diem.count(i)
        if(count > 10):
            print(str(i).strip(), ": ", count)
    print("---------------Tổng số địa điểm tuyển dụng là: ",len(set(list_dia_diem)))
    fdist_dia_diem = FreqDist(list_dia_diem)  # tuần suất xuất hiện
    fdist_dia_diem.plot(10)  # vẽ biểu đồ top 10 địa điểm

if __name__ == '__main__':
    thong_ke_nganh_nghe(nganh_nghe)