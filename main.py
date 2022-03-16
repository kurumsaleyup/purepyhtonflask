from flask import Flask
from flask import url_for

print(__name__)
app = Flask(__name__)


# rest API

@app.route('/')
def index():
    return 'index'


# hello world
@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


# if there is a change in the root URL of your app then you have to change it in every page where the link is present.
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run()
