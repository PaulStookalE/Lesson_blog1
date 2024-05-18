# Створюємо таблицю posts.

from datetime import datetime
from .base import BASE
from sqlalchemy import Column, String, Integer, DateTime, Text



class Post(BASE):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now())      # DateTime -- видає точний час і день створення.
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable= False)                 # Text -- це той самий String, проте він має більшу місткість символів.


    # __init__ тут потрібен для того щоб поля title і content були обов'язково заповненими.
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
