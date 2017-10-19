#coding:utf-8

'''
    step1:
        create_iroya_data = create_data("./result", "iroya_data.csv")
        create_iroya_data.run()
        调用函数，从result文件夹内读取每个图片的名称，并将图片名和描述信息保存到iroya_data.csv
    step2:
        python test.py 获取推荐结果
'''
import csv
import os
from googletrans import Translator

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def trans_csv():
    csv_reader = csv.reader(open('jp_en.csv'))
    for row in csv_reader:
        #strs = (str(row)).split(',')
        num = row[0]
        num = num.encode('utf-8')
        str_keyword = row[1]
        tmp = str_keyword.encode('utf-8')
        tmp = tmp.replace(' ',',')
        str1s = tmp.split(',')
        res = ''
        for str1 in str1s:
            try:
                translated = Translator().translate(str1,dest='en')
                res = res + translated.text + ' '
            except:
                print (str1 + "***")
        
        res = num + ',' + res
        print res

        fd = open('save_data.csv','a')
        fd.write('\n' + res)
        fd.close()


trans_csv()




        