import sqlite3
def Search():
    Search_words = str(input("Nhập từ khoá tìm kiếm: "))
    Search_words = "%{}%".format(Search_words)

    conn = sqlite3.connect("data/DBTimviec.db")
    query = """SELECT TITLE,LINK, DESCRIPTION from JOBS_DATA 
        where CONTENT like ? OR TITLE LIKE ? OR JOB_NAME LIKE ? OR DESCRIPTION LIKE ?
    """
    a = conn.execute(query,(Search_words,Search_words,Search_words,Search_words)).fetchall()
    conn.commit()
    for i in a:
        print("--------------------------------------------")
        for item in i:
            print(item)
if __name__ == '__main__':
    Search()

