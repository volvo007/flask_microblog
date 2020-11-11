from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sing in')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validatiors=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password Repeat', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # 这里的两个自定义函数，主要作用是，除了上面的限制，还需要满足这两个自定义函数才能通过验证
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different name')

    def validate_email(self, email):
        user = User.query.filter_by(email=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different email')
