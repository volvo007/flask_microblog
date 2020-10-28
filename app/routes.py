from app import app # 第二个 app 是 init文件里的app 对象
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'b day'
            },
            {
                'author': {'username': 'Lucy'},
                'body': 'bbb day'
            }
        ]
