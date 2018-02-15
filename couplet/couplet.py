# coding: utf-8
import json
from flask import Flask, Response
from flask import render_template, redirect, url_for
from flask import request
from flask import jsonify

app = Flask(__name__)

Str = "运在艳好老寿到好习到气景彩高旺云春户世岁业节意图和暖阵物瑞翠丽乐福"


@app.route('/')
def hello_world():
    return render_template('spring.html')


@app.route('/spring', methods=['POST'])
def spring():
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        value = data['value'].strip()
        value = value[-1]
        if value in Str:
            result = {
                'value': "这是一个上联，上联在右侧门哦",
            }
        else:
            result = {
                'value': "这是一个下联，上联在左侧门哦",
            }
        return jsonify(result)
    return render_template('spring.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
