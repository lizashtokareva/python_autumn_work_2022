# todo: добавьте во Flask маршруты для страниц (endpoint)
# О компании
# Контакты
# Список постов

from flask import Flask
app = Flask(__name__)
@app.route('/about')
def about():
    return '<h1>О компании<h1>'


@app.route('/contacts')
def contacts():
    return '<h1>Контакты<h1>'

@app.route('/posts')
def posts():
    return '<h1>Список постов<h1>'

if __name__ == '__main__':
    app.run(debug=True)