from app.web import web
from flask import render_template, request


@web.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        print(request.form['username'])
        return render_template('index.html')
    return render_template('login.html')
