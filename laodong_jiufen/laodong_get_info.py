from lxml import etree
import os
def get_info(dir,filename):
    xml_file = etree.parse(os.path.join(dir,filename))
    root_node = xml_file.getroot()
    str1=""
    str2=""
    str3=""
    str4=""
    str5_1=""
    str5_2=""
    str6=""
    str7=""
    str8=""
    str9=str10=str11=str12=""
    node1 = xml_file.xpath("/write/LDJFYSTQ/LDZGZGW/SSGZGW/Value")
    if node1[0].text:
        str1=node1[0].text
    node2_1 = xml_file.xpath("/write/LDJFYSTQ/GZGSZDYJGZGC/HTYD/GSZD")
    if node2_1:
        str2=node2_1[0].text
    node2_2 = xml_file.xpath("/write/LDJFYSTQ/GZGSZDYJGZGC/YGZZ/GSZD")
    if node2_2:
        str3=node2_2[0].text
    node2_3 = xml_file.xpath("/write/LDJFYSTQ/GZGSZDYJGZGC/BGKB/GSZD")
    if node2_3:
        str4=node2_3[0].text
    node2_4_1 = xml_file.xpath("/write/LDJFYSTQ/GZGSZDYJGZGC/ZJ/YGZJ/*")
    if node2_4_1:
        for temp_node in node2_4_1:
            str5_1 = str5_1+temp_node.text
    node2_4_2 = xml_file.xpath("/write/LDJFYSTQ/GZGSZDYJGZGC/ZJ/BGZJ/*")
    if node2_4_2:
        for temp_node in node2_4_2:
            str5_2 = str5_2+temp_node.text
    node2_5 = xml_file.xpath("/write/LDJFYSTQ/GZGSZDYJGZGC/FYRD/GSZD")
    if node2_5:
        str6=node2_5[0].text
    node3 = xml_file.xpath("/write/LDJFYSTQ/GSQK/GSRDQK/*")
    for temp_node in node3:
        str7=str7+temp_node.text+'。'
    node4 = xml_file.xpath("/write/LDJFYSTQ/SCDJJD/*")
    for temp_node in node4:
        str8=str8+temp_node.text+'。'
    node5 = xml_file.xpath("/write/LDJFYSTQ/SJFYLX/*")
    for temp_node in node5:
        str9 =str9 + temp_node.text+'。'
    node6 = xml_file.xpath("/write/LDJFYSTQ/ZCQQ/Value")
    if node6[0].text:
        str10=node6[0].text
    node7 = xml_file.xpath("/write/LDJFYSTQ/ZCJG/Value")
    if node7[0].text:
        str11=node7[0].text
    node8 = xml_file.xpath("/write/LDJFYSTQ/YGSSQQ/Value")
    if node8:
        str12=node8[0].text
    # print(str1)
    # print(str2)
    # print(str3)
    # print(str4)
    # print(str5_1)
    # print(str5_2)
    # print(str6)
    # print(str7)
    # print(str8)
    # print(str9)
    # print(str10)
    # print(str11)
    # print(str12)
    return str1+str2+str3+str4+str5_1+str5_2+str6+str7+str8+str9+str10+str11+str12



