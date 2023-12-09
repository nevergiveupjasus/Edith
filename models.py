from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime


class User(Base):
    __tablename__ = "users_messages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    message_subject = Column(String(80))
    message = Column(String(800))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


