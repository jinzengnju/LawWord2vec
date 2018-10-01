import gensim
import os

from getOriginalData import fenc
from lihun_jiufen import lihun_get_info


def get_new_file_words(dir):
    filename = os.listdir(dir)
    sentences = []
    text1 = fenc.seg_word(lihun_get_info.get_info(dir, filename[0]))
    text2 = fenc.seg_word(lihun_get_info.get_info(dir, filename[1]))
    text1_once = set(word for word in set(text1) if text1.count(word) <5)
    text1_out = [word for word in text1 if word not in text1_once]
    text2_once = set(word for word in set(text2) if text2.count(word) <5)
    text2_out = [word for word in text2 if word not in text2_once]
    sentences.append(text1_out)
    sentences.append(text2_out)
    return sentences

sentences=get_new_file_words(r'E:/提取要素/离婚纠纷/修改后/ceshi')
print(sentences)
print(sentences[0].__sizeof__())
print(sentences[1].__sizeof__())
new_model = gensim.models.Word2Vec.load('E:/Python_exercise/LawWord2vec/model/result_lihun.model')
print(len(new_model.wv.vocab))
new_model.build_vocab(sentences,update=True)
new_model.train(sentences)
print(len(new_model.wv.vocab))
print(new_model.n_similarity(sentences[0],sentences[1]))