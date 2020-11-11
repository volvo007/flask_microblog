import time
from flask import render_template, flash, redirect, url_for
from flask.globals import request
from flask_login.utils import logout_user
from werkzeug.urls import url_parse
# from flask.helpers import flash # 闪动消息
from app import app, db # 第二个 app 是 init文件里的app 对象
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required # 登录保护只需要加一个装饰器，加了这个的，都必须登录才能访问
def index():
    # user = {'username': 'Miguel'}
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
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: # login 模块会默认创建一个用户为 current_user
        return redirect(url_for('index')) # 如果登录成功，会被跳转到主页
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # 数据库查询用户
        # 这里查询用户，或者没有，或者密码不对
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # remember_me 用 cookie 保留登录状态
        login_user(user, remember=form.remember_me.data)

        # 虽然没有登录的用户会重定向到 login，不过会包含三种情况
        # 1. 登录url没有 next 参数，则重定向到 /login
        # 2. 登录url包含 next 设置为相对路径的参数，则重定向到该url
        # 3. 登录url包含 next 设置为包含域名的完整 url 的参数，则重定向到 /index
        # 这是为了保证，重定向只发生在站内，不会导向恶意网站
        # 为了只发生1，2，要调用 werkzeug 的 url_parse 解析
        # 举例，如果登录失败，会出现 login?next=%2Findex ，%2F 是 / 字符，也就是重定向到 index
        # 不过因为没有登录，所以这个行为会被接着重定向回 login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrates, you now registered a new user')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)