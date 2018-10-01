import gensim
import os

from getOriginalData import fenc
from laodong_jiufen import laodong_get_info
#https://blog.csdn.net/u010665216/article/details/78709018
#这篇博客讲述了当数据量太大时，可以采用迭代器的方法加载数据

def get_corpus():
    corpus=[]
    for newfile in filename:
        text = fenc.seg_word(laodong_get_info.get_info(dir, newfile))
        print(text)
        corpus.append(text)
    return corpus

dir = r'C:\Users\Jin\Desktop\文书阅读'
filename=os.listdir(dir)
sentences=get_corpus()
model = gensim.models.Word2Vec(sentences,size=200)
model.save('E:/Python_exercise/LawWord2vec/model/result2.model')