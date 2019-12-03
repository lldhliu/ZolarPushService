from wtforms import PasswordField, Form
from wtforms.validators import DataRequired


class LoginForm(Form):
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空, 请输入你的密码')
    ])