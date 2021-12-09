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
    flask
'''
from flask import Flask,render_template,request,jsonify
import pandas as pd
import os

path = 'D:/chatbot201_21Capstone'
os.chdir(path)
chatbot_data = pd.read_csv('./chatbot_data_csv.csv')
chat_dic = {}
row = 0
for rule in chatbot_data['rule']:
    chat_dic[row] = rule.split('|')
    row += 1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

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

@app.route("/ask/<text>", methods=['POST'])
def ask(text: str):
    message = text
    response = chat(message)

    while True:
        if '안녕' in message:
            response = '안녕하세요. 저는 서울과학기술대학교 학군단 챗봇 Chatbot-201입니다.'
            return jsonify({'status':'OK','answer':response})
        elif '고마워' in message:
            response = '천만에요. 더 물어보실 건 없나요?'
            return jsonify({'status':'OK','answer':response})
        elif '없어' in message:
            response = '그렇군요. 알겠습니다!'
            return jsonify({'status':'OK','answer':response})
        else:
            return jsonify({'status':'OK','answer':response})

if __name__ == '__main__':
    #app.template_folder = os.curdir + 'templates'
    app.template_folder = os.path.join(os.curdir, 'templates')
    app.static_folder = os.path.join(os.curdir,'static')
    app.run(port=8080, host='0.0.0.0')