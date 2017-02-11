from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('home.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/something')
def something():
    return app.send_static_file('something.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/post/<postnum>')
def post(postnum):
    return 'This is post' + postnum
