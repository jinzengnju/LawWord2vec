# -*- coding=gbk -*-

"""
     ԭʼ���ݣ����ڽ���ģ��
"""

# ��ˮ���courses��ʵ�����ݵĸ�ʽӦ��Ϊ �γ���\t�γ̼��\t�γ����飬����ȥ��html�ȸ�������
import jieba.analyse
from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import os
import nltk
import  sys
sys.path.append("E:/Python_exercise/�����ļ���")
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
    u'û��\��������',
    u'û��\t��������',
    u'û��\t��������',
    u'û��\t����������',
    u'û��',
    u'����û��',
    u'Ҳû��',
    u'��û��Ҳ����',
    u'Angry Birds Stella',
    u'Flappy Wings - FREE\tFly into freedom!A parody of the #1 smash hit game!',
    u'û��һ��',
    u'û��һ��2',
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

    # ȥ��������
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if not word in english_punctuations] for document in
                      texts_filtered_stopwords]

    # �ʸɻ�
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in document] for document in texts_filtered]

    # ȥ������Ƶ�ʴ�
    if low_freq_filter:
        all_stems = sum(texts_stemmed, [])
        stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
        texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
        print("��ɹ���")
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
# �⽨�����---�ò����������󣬿�Ԥ�ȴ���ã��洢����
    (index, dictionary, lsi) = train_by_lsi(lib_texts)

# ѡ��һ����׼����
target_courses = [u'û��']
target_text = pre_process_cn(target_courses, low_freq_filter=False)


�Ծ���������ƶ�ƥ��


# ѡ��һ����׼����
ml_course = target_text[0]
# �ʴ�����
ml_bow = dictionary.doc2bow(ml_course)
# ������ѡ���ģ������ lsi �У���������������������ƶ�
ml_lsi = lsi[ml_bow]  # ml_lsi ��ʽ�� (topic_id, topic_value)
sims = index[ml_lsi]  # sims �����ս���ˣ� index[xxx] �������÷��� __getitem__() ������ml_lsi
# ����Ϊ�������
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])

# �鿴���
print(sort_sims[0:10])  # ����ǰ10�������Ƶģ���һ���ǻ�׼��������
print(courses_name[sort_sims[1][0]])  # ����ʵ�������Ƶ����ݽ�ʲô
print(courses_name[sort_sims[2][0]])  # ����ʵ�������Ƶ����ݽ�ʲô
print(courses_name[sort_sims[3][0]])  # ����ʵ�������Ƶ����ݽ�ʲô
'''