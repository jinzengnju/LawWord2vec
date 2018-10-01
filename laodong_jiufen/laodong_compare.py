import gensim
import os

from getOriginalData import fenc
from laodong_jiufen import laodong_get_info


def get_new_file_words(dir):
    filename = os.listdir(dir)
    sentences = []
    text1 = fenc.seg_word(laodong_get_info.get_info(dir, filename[4]))
    text2 = fenc.seg_word(laodong_get_info.get_info(dir, filename[5]))
    text1_once = set(word for word in set(text1) if text1.count(word) <5)
    text1_out = [word for word in text1 if word not in text1_once]
    text2_once = set(word for word in set(text2) if text2.count(word) <5)
    text2_out = [word for word in text2 if word not in text2_once]
    sentences.append(text1_out)
    sentences.append(text2_out)
    return sentences

sentences=get_new_file_words(r'C:/Users/Jin/Desktop/文书阅读')
print(sentences)
print(sentences[0].__sizeof__())
print(sentences[1].__sizeof__())
new_model = gensim.models.Word2Vec.load('E:/Python_exercise/LawWord2vec/model/result.model')
print(len(new_model.wv.vocab))
new_model.build_vocab(sentences,update=True)
new_model.train(sentences)
print(new_model.wordvecs(sentences[0]))

# print(len(new_model.wv.vocab))
# print(new_model.n_similarity(sentences[0],sentences[1]))

# dir = r'C:/Users/Jin/Desktop/文书阅读/online'
# filename=os.listdir(dir)
# text1=fenc.seg_word(get_info_yaosu.get_info(dir, filename[0]))
# text2=fenc.seg_word(get_info_yaosu.get_info(dir, filename[1]))
# sentences=[]
# sentences.append(text1)
# sentences.append(text2)
# new_model = gensim.models.Word2Vec.load('E:/Python_exercise/LawWord2vec/model/result2.model')
# new_model.train(sentences)
# import os
# os.chdir('E:/pythontest')
# import nltk
# nltk.data.path.append('./NTLK/DownloadFromInternet/nltk_data/')

