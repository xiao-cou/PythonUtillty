# -*- coding: utf-8 -*-

import datetime

begin = datetime.datetime.now()
result_dic = dict()
line_dict_unique = dict()
with open('E:\\pythonSpace\\Crawling\\data\\40624md5.txt', 'r') as fd:
    for line in fd:
        #取line的前14位
        key = line[0: 14]
        #取最后两位
        category = line[14: 16]
        if key not in line_dict_unique.keys():
            #添加文件内容到两个字典中
            line_dict_unique[key] = category
            result_dic[key] = category
        else:
            continue
# print(line_dict_unique)
# print(len(line_dict_unique))

with open("E:\\pythonSpace\\Crawling\\data\\10000000", "r") as big:
    for line in big:
        big_key = line[0: 14]
        big_category = line[14: 16]
        if len(result_dic) != 10000000:
            if big_key in line_dict_unique.keys():
                continue
            else:
                result_dic[big_key] = big_category

with open('E:\\pythonSpace\\Crawling\\data\\result', 'w') as f:
    for key, value in result_dic.items():
        f.write(key + str(value))
        f.write('\n')

end = datetime.datetime.now()
duration = (end - begin).seconds
print("Distinct finished. duration: " + str(duration) + "s")
