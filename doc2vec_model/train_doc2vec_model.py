import gensim
from gensim import utils
from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence
from os import listdir
from os.path import isfile, join

from getOriginalData import fenc
from getOriginalData.QW_info import get_QW_info


def get_TextData(docLabels):
    data=[]
    for doc in docLabels:
        text= fenc.seg_word(get_QW_info(r'E:/提取要素/离婚纠纷/修改后/ceshi', doc))
        data.append(text)
    return data

class LabeledLineSentence(object):
    def __init__(self,labels_list,data):
        self.labels_list=labels_list
        self.data=data
    def __iter__(self):
        for idx,doc in enumerate(data):
            yield LabeledSentence(words=doc,tags=[self.labels_list[idx]])
    # def to_array(self):
    #     self.texts=[]
    #     for idx,doc in enumerate(data):
    #         self.texts.append(LabeledSentence(words=doc,tags=[self.labels_list[idx]]))
    #     return self.texts

#巡联模型
if __name__=='__main__':
    # docLabels=[]
    # docLabels=[f for f in listdir(r"E:/提取要素/离婚纠纷/修改后/ceshi")]
    # data=get_TextData(docLabels)
    # it=LabeledLineSentence(docLabels,data)
    # model=Doc2Vec(size=200, window=10, min_count=5,alpha=0.025, min_alpha=0.025)
    # model.build_vocab(it)
    # for epoch in range(10):
    #     model.train(it)
    #     model.alpha -= 0.002  # decrease the learning rate
    #     model.min_alpha = model.alpha  # fix the learning rate, no deca
    #     model.train(it)
    # model.save("E:/Python_exercise/LawWord2vec/modeldoc2vec.model")
    # print(model.docvecs["(2006)西民一初字第64号民事判决书（一审民事案件用）.doc.xml要素提取.xml"])



    new_model = gensim.models.Doc2Vec.load('E:/Python_exercise/LawWord2vec/modeldoc2vec.model')
    print(new_model.docvecs["(2006)西民一初字第64号民事判决书（一审民事案件用）.doc.xml要素提取.xml"])
    #print(new_model.infer_vector("我爱南京大学"))





