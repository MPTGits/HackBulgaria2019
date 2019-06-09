from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship, backref
from .main_database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)
    status=Column(String)
    

    def __init__(self, username, hashed_password,status=None):
        self.username= username
        self.hashed_password=hashed_password
        self.status=status

