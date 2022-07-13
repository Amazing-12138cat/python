#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# File      Name:去重-excel-txt.py
# Author:   XXXX
# Date:     2022/7/12 16:40
'''

import pandas as pd             #need install :pip install pandas
lists = []
txt_name = 'ip.txt'             ##edit
excel_name = 'ip.csv'           ##edit,cxv\xlsx\xls

def read_csv():
    data = pd.read_csv(excel_name,index_col=False)
    row = data.values
    for i in row:
        lists.append(i[0])          ##according to col number
def read_xlsx():
    data = pd.read_excel(excel_name,sheet_name='Sheet1')
    row = data.values
    for i in row:
        lists.append(i[0])          ##according to col number
for line in open(txt_name,mode='r'):
    lists.append(line.replace('\n', ''))
if 'csv' in excel_name:
    read_csv()
elif 'xls' in excel_name:
    read_xlsx()
else:
    print('[-] file type error!')

result = list(set(lists))
with open('ip_result.txt',mode='w+') as f:
    for ip in result:
        f.write(ip+'\n')
