# c1 thêm file stopword vào thư viện stopword của nltk
#from nltk.corpus import stopwords
#cachedStopWords = stopwords.words("stopword_vietnam_ne")


# c2 tạo stopword
stopwords_vietnam = []
with open('stopword_vietnam_ne.txt', 'r',encoding="utf8") as f:
    for line in f:
        stopwords_vietnam.append(line.strip())

def loai_bo_stopword(text):
    text = ' '.join([word for word in text.split() if word not in stopwords_vietnam])
    return text
if __name__ == "__main__":
    print(loai_bo_stopword("ý là tuyến rất thích học python á"))