from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash

from app.models.base import Base


class User(Base):
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
