# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)


@app.route('/add')
def calc_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = add(a, b)
    return f"a: {a} + b: {b} = {total}"

@app.route('/sub')
def calc_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = sub(a, b)
    return f"a: {a} + b: {b} = {total}"

@app.route('/mult')
def calc_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = mult(a, b)
    return f"a: {a} + b: {b} = {total}"

@app.route('/div')
def calc_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = div(a, b)
    return f"a: {a} + b: {b} = {total}"


####### MY SOLUTION ##########

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    if operation == 'add':
        total = add(a, b)
    elif operation == 'sub':
        total = sub(a, b)
    elif operation == 'mult':
        total = mult(a, b)
    elif operation == 'div':
        total = div(a, b)

    return f"a: {a} operation b: {b} = {total}"


####### COURSE SOLUTION ##########

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)