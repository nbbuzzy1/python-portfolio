from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/')
# def my_home():
#     return render_template('index.html')


# @app.route('/index.html')
# def my_home2():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')
