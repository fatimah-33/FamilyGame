# -- import --
import os
from distutils.debug import DEBUG
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
# Using a development configuration


@app.route('/')
@app.route('/startgame')
def startGame():
    return render_template('game.html')


@app.route('/question1')
def question1():
    return render_template('question1.html')


@app.route('/question2')
def question2():
    return render_template('question2.html')


@app.route('/question3')
def question3():
    return render_template('question3.html')


@app.route('/question4')
def question4():
    return render_template('question4.html')


@app.route('/question5')
def question5():
    return render_template('question5.html')


@app.route('/question6')
def question6():
    return render_template('question6.html')


@app.route('/question7')
def question7():
    return render_template('question7.html')

@app.route('/question8')
def question8():
    return render_template('question8.html')


if __name__ == '__main__':
    app.run(DEBUG=True)
