from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/<username>/<int:user_id>')
def hello_world(username=None, user_id=None):
    return render_template('index.html', name=username, user_id=user_id)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/favicon.ico')
def blog():
    return 'These are my thoughts on blogs'


@app.route('/blog/2020/dogs')
def blog2():
    return 'this is my dog'
