from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

# Створюємо додаток Flask.
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')



# Імортуємо роути (шляхи) із файлу 'routes.py'
from . import routes



# Запускаємо програму.
if __name__ == '__main__':
    app.run(debug=True)



# # #       Щоб запустити проект через термінал:
                        # 1. Активувати віртуальне середовище.
                        # 2. set FLASK_APP=__init__.py
                        # 3. flask run