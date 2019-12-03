from app.forms.user import LoginForm
from app.models.user import User
from app.web import web
from flask import render_template, request


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # print(request.method)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(phone=form.phone.data).first()
        if user and user.check_password(form.password.data):
            pass
        return render_template('index.html')
    return render_template('login.html')
