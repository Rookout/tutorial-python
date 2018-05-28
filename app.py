from rook import auto_start
import flask
import re
import os
import string
import random
import json
from todos_store import Store

app = flask.Flask(__name__, static_url_path='/static')

# unsafeRandId generates a random string composed from english upper case letters and digits
# it's called unsafe because it doesn't use a crypto random generator


def unsafeRandId(len):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len))


def cleanStr(str):
    return re.sub(r'[>|<|;|`|&|/|\\]', '', str)

# redirect from base url to index.html


@app.route("/")
def index():
    return flask.redirect('/static/index.html')


@app.route('/todos/<todoId>', methods=['DELETE'])
def del_todo(todoId):
    todos = Store.getInstance().todos
    newTodos = [t for t in todos if t['id'] != todoId]
    todos = newTodos
    return ('', 204)


@app.route('/todos/clear_completed', methods=['DELETE'])
def clear_completed():
    todos = Store.getInstance().todos
    todo = [t for t in todos if not t['completed']]
    return ('', 204)


@app.route('/todos', methods=['UPDATE'])
def update_todo():
    todos = Store.getInstance().todos
    req = flask.request
    todo = req.get_json()
    for t in todos:
        if t['id'] == todo['id']:
            t['title'] = todo['title']
            t['completed'] = todo['completed']
            break
    return ('', 204)

# add a new todo action


@app.route('/todos', methods=['POST'])
def add_todo():
    todos = Store.getInstance().todos
    fr = flask.request
    req = fr.get_json()
    todoStr = cleanStr(req['title'])
    if not todoStr:
        return ('', 400)
    todo = {
        "title": cleanStr(req['title']),
        "id": unsafeRandId(10),
        "completed": False
    }
    todos.append(todo)
    return ('', 204)


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Store.getInstance().todos
    return json.dumps(todos)


@app.route('/todo/dup/<todoId>', methods=['POST'])
def duplicate_todo(todoId):
    todos = Store.getInstance().todos
    for todo in todos:
        if todoId == todo['id']:
            todos.append(
                {'title': todo['completed'],
                 'id': unsafeRandId(10),
                 'completed': todo['title']})
            break
    return ('', 204)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
