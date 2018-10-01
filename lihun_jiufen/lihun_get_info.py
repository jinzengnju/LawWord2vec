from lxml import etree
import os
def get_info(dir,filename):
    xml_file = etree.parse(os.path.join(dir,filename))
    root_node = xml_file.getroot()
    str1=""
    str2=""
    str3=""
    str4=""
    str5=""
    str6=""

    node1 = xml_file.xpath("/write/LHJHYSTQ/JBSS/FQBHDKSSJJYY/FQBHKSYY")
    if node1[0].get("value")!="未提及":
        str1=node1[0].get('value')

    node2 = xml_file.xpath("/write/LHJHYSTQ/JBSS/FJQK/KSFJYY")
    if node2[0].get("value")!="未提及":
        str2=node2[0].get('value')

    node3 = xml_file.xpath("/write/LHJHYSTQ/ZVFYQGSXCMSS/*")
    for i in range(4):
        if node3[i].get('value')!="未提及":
            str3=str3+node3[i].get('value')

    node4=xml_file.xpath("/write/LHJHYSTQ/CCFGXCMSS/*")
    for i in range(2):
        if node4[i].get('value') != "未提及":
            str4=str4+node4[i].get('value')

    node5 = xml_file.xpath("/write/LHJHYSTQ/CCFGXCMSS/FQGTCC/*")
    for i in range(5):
        if node5[i].get('value') != "未提及":
            str5=str5+node5[i].get('value')

    node6 = xml_file.xpath("/write/LHJHYSTQ/FQGTZQZWQK/*")
    for temp_node in node6:
        if temp_node.get('value') != "未提及":
            str6 = str6 + temp_node.get('value')

    # print(str1)
    # print(str2)
    # print(str3)
    # print(str4)
    # print(str5)
    # print(str6)

    str_temp = str1+str2+str3+str4+str5+str6
    new_model = gensim.models.Doc2Vec.load('E:/Python_exercise/LawWord2vec/modeldoc2vec.model')
    mylist=new_model.infer_vector(str_temp)
    return mylist
# if __name__=='__main__':
#     get_info(r'E:/提取要素/离婚纠纷/修改后\离婚纠纷文书要素提取','(2015)宝民初字第1959号民事判决书（一审民事案件用）.doc.xml要素提取.xml')

