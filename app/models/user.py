from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base
from flask_login import UserMixin


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), comment='用户名')
    phone = Column(String(50), unique=True, index=True, comment='手机号')
    gender = Column(String(50), comment='性别')
    age = Column(Integer, comment='年龄')
    address = Column(String(255), comment='用户地址')
    # role = Column(String(50), comment='用户角色')

    _password = Column(String(255), comment='password')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    # # flask_login 要求的在用户模型内部定义的函数,定义用什么来表示用户身份
    # 上面继承了 User
    # def get_id(self):
    #     return self.id
