from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

class Reminder(db.Model):
    __tablename__ = 'reminder'
    id = Column(Integer, primary_key=True)
    message = Column(String(100), nullable=False)
    time =  Column(String(5), nullable=False)