from flask import Flask, request
from operations import sub, mult, div, add

app = Flask(__name__)


@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a,b)

    return str(result)

@app.route('/sub')
def subtraction():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a,b)

    return str(result)

@app.route('/mult')
def multiplication():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a,b)

    return str(result)

@app.route('/div')
def division():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a,b)

    return str(result)


operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
@app.route('/math/<option>')
def math(option):
    # a = int(request.args['a'])
    # b = int(request.args['b'])
    result = operations[option](int(request.args['a']), int(request.args['b']))
    return str(result)
   
    # result = operations[option](a,b)
    # return func(request.args['a'], request.args['b'])


# Put your app in here.
