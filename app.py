from flask import Flask
app = Flask(__name__)
from flask import url_for

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name