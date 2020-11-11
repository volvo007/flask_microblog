from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login  = LoginManager(app)
login.login_view = 'login' # 登录保护功能，如果没有登录，则跳转到饿视图

print('{} is using me'.format(__name__))

from app import routes, models