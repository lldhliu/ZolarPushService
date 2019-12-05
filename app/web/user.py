from app.forms.user import LoginForm
from app.models.user import User
from app.web import web
from flask import render_template, request, flash
from flask_login import login_user


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(form.data, type(form.data))
    if request.method == 'POST' and form.validate():
        print(form.password.data)
        user = User.query.filter_by(phone=form.phone.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            pass
        else:
            flash('账号不存在或密码错误')
        return render_template('index.html')
    print(form.errors)
    return render_template('login.html')
