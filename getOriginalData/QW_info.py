from lxml import etree
import os
def get_QW_info(dir,filename):
    xml_file = etree.parse(os.path.join(dir, filename))
    root_node = xml_file.getroot()
    node1 = xml_file.xpath("/write/QW")
    str = node1[0].get('value')
    return str



# if __name__=='__main__':
#     str=get_QW_info(r'E:/提取要素/离婚纠纷/修改后/ceshi','(2006)西民一初字第64号民事判决书（一审民事案件用）.doc.xml要素提取.xml')
#     print(str)