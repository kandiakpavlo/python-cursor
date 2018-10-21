from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender):
    response_data = {"jsonrpc": "2.0"}
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    response_data["result"] = f"We add your member {MEMBERS[name]}"
    return json.dumps(response_data)


def get_member(name):
    response_data = {"jsonrpc": "2.0"}
    response_data['result'] = MEMBERS[name]
    return json.dumps(response_data)


METHODS = {
    "getMember": get_member,
    "addMember": add_member
}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}})

    result = method_view(**data.get("params"))
    return result

@app.route('/ping', methods=['POST'])
def ping():
    data = json.loads(request.data.decode('utf-8'))
    if data.get('method') != 'ping':
        return json.dumps({'error': {'code': -32601, 'message': 'Method not found'}})
    result = {'jsonrpc': '2.0', 'result': 'pong'}
    return json.dumps(result)   

if __name__ == '__main__':
    app.run(port=4001, host="127.0.0.1", debug="True")
