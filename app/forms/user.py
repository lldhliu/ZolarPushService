from wtforms import PasswordField, Form, StringField
from wtforms.validators import DataRequired, Regexp, Length


class LoginForm(Form):
    phone = StringField(validators=[Regexp(r'1[85347]\d{9}', message='手机号码格式不正确')])

    password = PasswordField('密码', validators=[
        Regexp(r'^[a-z0-9][a-z0-9_]{5}$', message='密码里面只能包含大小写字母、数字、_，且不能以“_”开头'),
        DataRequired(message='密码不可以为空, 请输入你的密码'),
        Length(6, 6, message='密码长度必须为6个字符')
    ])
