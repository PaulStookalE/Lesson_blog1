# Створюємо файл із функціями і екземплярами класів для створення і видалення БД.

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE = create_engine(os.getenv('DATABASE'))


Session = sessionmaker(DATABASE)
session = Session()


BASE = declarative_base()


def create_db():
    BASE.metadata.create_all(DATABASE)

def drop_db():
    BASE.metadata.drop_all(DATABASE)