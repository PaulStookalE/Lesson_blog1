# Створюємо файл зі шляхами, який потім імпортуємо у __init__.py.
from . import app
from flask import render_template, request, redirect
from .models import Post, session
from dotenv import load_dotenv


load_dotenv()


# Виймаємо всі пости із БД і надсилаємо їх у FrontEnd.
@app.route('/')
def read_all_posts():
    all_posts = session.query(Post).all()
    return render_template('index.html', all_posts=all_posts)



# Виймаємо деталі конкретного посту із БД і передаємо їх у FrontEnd.
@app.route('/read_post_detail/<int:id>')        # Користувач має додати у запиті на вебсайт id поста, щоб дізнатися деталі.
def read_post(id):
    post = session.query(Post).get(id)
    return render_template('post_detail.html', post=post)


# Створюємо пост, отримуючи дані із формочки із FrontEndу.
@app.route('/create_post', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        content = request.form['content']
        title = request.form['title']
        
        new_post = Post(
            content=content,
            title=title
        )
        

        try:
            session.add(new_post)       # Перетворюємо дані від користувача у об'єкт.
            session.commit()            # Вносимо цей об'єкт у БД.
            return redirect('/')
        
        except Exception as exc:
            return f'При збереженні поста виникла помилка: {exc}'
        
        finally:
            session.close()             # Завершуємо сесію (ОБОВ'ЯЗКОВО!!!).


    else:
        return render_template('create_post.html')
    



# Оновлюємо вже існуючі поля у БД.
@app.route('/update_post/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    post = session.query(Post).get(id)

    if request.method == 'POST':
        content = request.form['content']
        title = request.form['title']

        if title or content:

            try:
                # *У рамках вже будуть виведені поточні значення, проте користувач матиме змогу їх змінити.*
                # Переприсвоюємо значення ключів title і content.
                post.title = title
                post.content = content
                session.commit()

                # Перенаправляємо користувача на інший роут.
                return redirect('/')
            
            except Exception as exc: 
                return f'При оновленні поста виникла помилка: {exc}'
            
            finally:
                session.close()
        else:
            return 'Онови поля, оскільки ти їх не змінив/ла.'
    else:
        return render_template('update_post.html', post=post)
    



# Видаляєсо конкретний пост.
@app.route('/delete_post/<int:id>')
def delete_post(id):

    # Відфільтровуємо пости по id.
    post = session.query(Post).get(id)

    if post:
        session.delete(post)
        session.commit()
        session.close()
        return redirect('/')