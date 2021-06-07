from flask import Flask, request
from app import sum, difference, multiply, divide

app = Flask(__name__)

@app.route("/sum", methods=[ 'GET'])
def addition():
    if request.method == 'POST':
        a = request.args.get('first')
        b = request.args.get('second')
        return str(sum(float(a), float(b)))

@app.route("/difference", methods=['POST', 'GET'])
def subtraction():
    if request.method == 'POST':
        a = request.args.get('first')
        b = request.args.get('second')
        return str(difference(float(a), float(b)))

@app.route("/product", methods=['POST', 'GET'])
def multiplication():
    if request.method == 'POST':
        a = request.args.get('first')
        b = request.args.get('second')
        return str(multiply(float(a), float(b)))

@app.route("/divide", methods=['POST', 'GET'])
def division():
    if request.method == 'POST':
        a = request.args.get('first')
        b = request.args.get('second')
        return str(divide(float(a), float(b)))

@app.route("/")
def home():
    return """For Addition go to \sum.\n
    For Subtraction go to \difference.\n
    For Multiplication go to \product.\n
    For Division go to \divide."""


if __name__ == "__main__":
    app.run(debug = True)