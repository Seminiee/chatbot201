# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 07:21:39 2021

@author: dani0
"""

'''
필요한 Python Package List:
    pandas
    os
    openpyxl
'''
import pandas as pd
import os

#path = 'E:/rotc질문모음'
path = 'C:/Users/dani0/Documents'
os.chdir(path)

chatbot_data = pd.read_excel('./chatbot_data.xlsx')
chat_dic = {}
row = 0
for rule in chatbot_data['rule']:
    chat_dic[row] = rule.split('|')
    row += 1


def chat(request): 
    for k, v in chat_dic.items(): 
        index = -1 
        for word in v: 
            try: 
                if index == -1: 
                    index = request.index(word) 
                else:
                
                    if index < request.index(word, index): 
                        index = request.index(word, index) 
                    else:
                        index = -1 
                        break 
            except ValueError: 
                index = -1 
                break 
        if index > -1: 
            return chatbot_data['response'][k] 
    return '질문을 이해하지 못했어요.'

while True:
    req = input('대화를 입력해보세요! : ')
    if req == 'exit':
        break
    else:
        print('201ROTC: ', chat(req))