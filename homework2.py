from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return str('September 1 1990')

@app.route('/greeting/<name>')
def greeting(name):
    return str('Hello %s' %name)

@app.route('/add/<num1>/<num2>/')
def plus(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    answer = num1 + num2
    finalanswer = str(answer)
    return finalanswer

@app.route('/multiply/<num1>/<num2>/')
def muiltiplications(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    mulanswer = num1 * num2
    return str(mulanswer)

@app.route('/subtract/<num1>/<num2>/')
def subtractions(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    subanswer = num1 - num2
    return str(subanswer)

@app.route('/favoritefoods')
def favoritefoods():
    foodlist = ['Garlic', 'Cheese', 'Spinach', 'Fish', 'Avocado']
    return jsonify(foodlist)

# @app.route('/add/<num1>/<num2>')
# def add(num1, num2):
#     num1 = int(num1)
#     num2 = int(num2)
#     # answer = num1 + num2
#     return str(num1 + num2)
