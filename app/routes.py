import time
from flask import render_template, flash, redirect, url_for
# from flask.helpers import flash # 闪动消息
from app import app # 第二个 app 是 init文件里的app 对象
from app.forms import LoginForm

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
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # msg = flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # print(msg)
        # time.sleep(2)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)