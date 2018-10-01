# -*- coding=gbk -*-

"""
     原始数据，用于建立模型
"""

# 缩水版的courses，实际数据的格式应该为 课程名\t课程简介\t课程详情，并已去除html等干扰因素
import jieba.analyse
from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import os
import nltk
import  sys
sys.path.append("E:/Python_exercise/备用文件夹")
courses = [
    u'Writing II: Rhetorical Composing',
    u'Genetics and Society: A Course for Educators',
    u'General Game Playing',
    u'Genes and the Human Condition (From Behavior to Biotechnology)',
    u'A Brief History of Humankind',
    u'New Models of Business in Society',
    u'Analyse Numrique pour Ingnieurs',
    u'Evolution: A Course for Educators',
    u'Coding the Matrix: Linear Algebra through Computer Science Applications',
    u'The Dynamic Earth: A Course for Educators',
    u'Tiny Wings\tYou have always dreamed of flying - but your wings are tiny. Luckily the world is full of beautiful hills. Use the hills as jumps - slide down, flap your wings and fly! At least for a moment - until this annoying gravity brings you back down to earth. But the next hill is waiting for you already. Watch out for the night and fly as fast as you can. ',
    u'Angry Birds Free',
    u'没有\它很相似',
    u'没有\t它很相似',
    u'没有\t他很相似',
    u'没有\t他不很相似',
    u'没有',
    u'可以没有',
    u'也没有',
    u'有没有也不管',
    u'Angry Birds Stella',
    u'Flappy Wings - FREE\tFly into freedom!A parody of the #1 smash hit game!',
    u'没有一个',
    u'没有一个2',
]
courses_name = courses
os.chdir("E:/pythontest")
nltk.data.path.append('./NTLK/DownloadFromInternet/nltk_data/')
def pre_process_cn(courses, low_freq_filter=True):
    texts_tokenized = []
    for document in courses:
        texts_tokenized_tmp = []
        for word in word_tokenize(document):
            texts_tokenized_tmp += jieba.analyse.extract_tags(word, 10)
        texts_tokenized.append(texts_tokenized_tmp)
    texts_filtered_stopwords = texts_tokenized
    print(texts_filtered_stopwords)

    # 去除标点符号
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if not word in english_punctuations] for document in
                      texts_filtered_stopwords]

    # 词干话
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in document] for document in texts_filtered]

    # 去除过低频率词
    if low_freq_filter:
        all_stems = sum(texts_stemmed, [])
        stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
        texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
        print("完成过滤")
    else:
        texts = texts_stemmed

    return texts

def train_by_lsi(lib_texts):
    dictionary = corpora.Dictionary(lib_texts)
    corpus = [dictionary.doc2bow(text) for text in lib_texts]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
    index = similarities.MatrixSimilarity(lsi[corpus])
    return (index, dictionary, lsi)


lib_texts = pre_process_cn(courses)


'''
# 库建立完成---该部分数据量大，可预先处理好，存储起来
    (index, dictionary, lsi) = train_by_lsi(lib_texts)

# 选择一个基准数据
target_courses = [u'没有']
target_text = pre_process_cn(target_courses, low_freq_filter=False)


对具体对象相似度匹配


# 选择一个基准数据
ml_course = target_text[0]
# 词袋处理
ml_bow = dictionary.doc2bow(ml_course)
# 在上面选择的模型数据 lsi 中，计算其他数据与其的相似度
ml_lsi = lsi[ml_bow]  # ml_lsi 形式如 (topic_id, topic_value)
sims = index[ml_lsi]  # sims 是最终结果了， index[xxx] 调用内置方法 __getitem__() 来计算ml_lsi
# 排序，为输出方便
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])

# 查看结果
print(sort_sims[0:10])  # 看下前10个最相似的，第一个是基准数据自身
print(courses_name[sort_sims[1][0]])  # 看下实际最相似的数据叫什么
print(courses_name[sort_sims[2][0]])  # 看下实际最相似的数据叫什么
print(courses_name[sort_sims[3][0]])  # 看下实际最相似的数据叫什么
'''