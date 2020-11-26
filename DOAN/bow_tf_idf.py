import sqlite3
import pandas as pd
def creat_word_count_dict():
    conn = sqlite3.connect("data/DBTimviec.db")
    query = """SELECT content FROM JOBS_DATA  limit 50"""
    a = conn.execute(query).fetchall()
    conn.commit()

    # tạo thư viện chứa các từ
    words = ""
    for item in a:
        for i in item:
            words += i

    words = words.split()
    words_dict = set(words)
    #print("Các từ trong nội dung: ",words_dict)
    words_count_dict = dict.fromkeys(words_dict, 0)

    # đếm số lượng từ xuất hiện trong thư viện
    for word in words:
        words_count_dict[word] += 1
    conn.close()
    return dict(words_count_dict)

def compute_TF(word_count_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_count_dict.items():
        tf_dict[word] = count/float(bow_count)

    return tf_dict


def compute_IDF(doc_list):
    import math
    idf_dict = {}
    N = len(doc_list)

    # đếm số lần xuất hiện của từ. Khởi tạo ban đầu bằng 0
    idf_dict = dict.fromkeys(doc_list.keys(), 0)

    for word, count in doc_list.items():
        if count > 0:
            idf_dict[word] += 1

    for word, count in idf_dict.items():
        idf_dict[word] = math.log(N / float(count))

    return idf_dict

def compute_TFIDF(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = val*idfs[word]
    return tfidf


def main():
    conn = sqlite3.connect("data/DBTimviec.db")
    query = """SELECT content FROM JOBS_DATA limit 1"""
    data = conn.execute(query).fetchall()
    conn.commit()

    bow = str(data).split(' ')
    word_dict = creat_word_count_dict()
    print(word_dict)
    # tính TF
    tf = compute_TF(word_dict,bow)
    print("Kết quả tf:",tf)
    # Tính IDF
    idf= compute_IDF(word_dict)
    print("Kết quả idf:",idf)
    #Cuối cùng: Tính TF-IDF Từ kết quả TF và IDF phía trên chỉ cần nhân lại là xong
    tf_idf = compute_TFIDF(tf,idf)
    print("Kết quả tf-idf:",tf_idf)

    # vẽ biểu đồ
    df = pd.DataFrame([tf_idf])
    #df.plot
if __name__ == '__main__':
    conn = sqlite3.connect("data/DBTimviec.db")
    query = """SELECT content FROM JOBS_DATA limit 1"""
    data = conn.execute(query).fetchall()
    conn.commit()

    bow = str(data).split(' ')
    word_dict = creat_word_count_dict()
    print(word_dict)
    # tính TF
    tf = compute_TF(word_dict,bow)
    print("Kết quả tf:",tf)
    # Tính IDF
    idf= compute_IDF(word_dict)
    print("Kết quả idf:",idf)
    #Cuối cùng: Tính TF-IDF Từ kết quả TF và IDF phía trên chỉ cần nhân lại là xong
    tf_idf = compute_TFIDF(tf,idf)
    print("Kết quả tf-idf:",tf_idf)

    # vẽ biểu đồ
    df = pd.DataFrame([tf_idf])
    #df.plot