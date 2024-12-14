from flask import Flask
from flask import request
import flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"


if __name__ == '__main__':
   app.run()