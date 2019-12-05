"""
 Created by ldh on 19-11-20
"""
from flask import Flask
from flask_login import LoginManager

__author__ = "ldh"

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)

    login_manager.init_app(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
