#_*_ coding:utf-8 _*_

import jieba.analyse
import re


def get_stopwords():
    fp=open('E:/Python_exercise/LawWord2vec/stopwords/stopwords.txt',encoding='utf-8')
    arr=[]
    for line in fp.readlines():
        if line:
            arr.append(line.strip())
    return arr

def seg_word(inputstr):
    stopword_list=get_stopwords()
    str_temp2=re.sub('[^(\\u4e00-\\u9fa5)]','',inputstr)
    str=re.sub('(?i)[^a-zA-Z0-9\u4E00-\u9FA5]','',str_temp2)
    word_list = jieba.cut(str)#word_list为一个生成器,生成器无列表的count函数
    out=[]
    for word in word_list:
        if word not in stopword_list:
            if len(word)>1:
                out.append(word)
    return out


'''
if __name__=='__main__':
    list=get_stopwords()
    print(list)
#print("Default Mode:", ' '.join(word_list))
'''

