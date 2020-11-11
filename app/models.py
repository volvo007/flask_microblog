from app import db, login # login 是 flask_login LoginManager 的一个类的实例
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
	# 继承 flask_login.UserMixin 之后（多继承），用户的一些必须属性就可以直接调用了
	# is_authorized, is_active, is_anonymous, get_id
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}'.format(self.body)

@login.user_loader
def load_user(id): # login 需要一个专门的函数获得数据库内信息
	return User.query.get(int(id)) # 这里 id 是一个字符串，所以需要转换