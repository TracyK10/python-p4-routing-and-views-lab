#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:username>')
def print_string(username):
    print(username)
    return username

@app.route('/count/<int:numbers>')
def count(numbers):
    for i in range(numbers):
        print(f'{i}\n')
    return f'<p>{numbers}</p>'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = str(num1 + num2)
    elif operation == '-':
        result = str(num1 - num2)
    elif operation == '*':
        result = str(num1 * num2)
    elif operation == 'div':
        result = str(num1 / num2)
    elif operation == '%':
        result = str(num1 % num2)
    else:
        result = 'Invalid operation'
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
