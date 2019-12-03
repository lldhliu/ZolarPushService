from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Community(Base):
    __tablename__ = 'community'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), comment='社区名称')
    no = Column(String(50), index=True, comment='社区代号')
    number = Column(String(50), comment='联系电话')
    description = Column(String(500), comment='社区描述')
