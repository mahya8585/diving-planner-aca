from flask import Flask
from flask import request
import agent
app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    # post bodyをjson型で取得
    data = request.get_json()

    # agentからのメッセージを取得
    #response_message = agent.orchastrator(data)




@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"


if __name__ == '__main__':
   app.run()