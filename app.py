import flask
import re
import string
import random
import json
from datetime import datetime
from random import randint
from todos_store import Store


from jaeger_client import Config
from flask_opentracing import FlaskTracer
from utils.logging import on_add_todo_logging, on_get_todos_logging
import os 
from flask import send_from_directory     






app = flask.Flask(__name__, static_url_path='/static')


# unsafeRandId generates a random string composed from english upper case letters and digits
# it's called unsafe because it doesn't use a crypto random generator
def unsafeRandId(len):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len))


def cleanStr(str):
    return re.sub(r'[>|<|;|`|&|/|\\]', '', str)

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through and send to Rookout
    rook.capture_exception(e)
    return e

@app.errorhandler(404)
def page_not_found(e):
    rook.capture_exception(e)    
    return '404 Page Not Found'


@app.errorhandler(500)
def internal_server_error(e):
    return '500 Internal Server Error'


@app.route("/error")
def render_bad_template():
    invalid_oper = 42 / 0    
    return flask.render_template('doesnotexist.html', number=invalid_oper)


# redirect from base url to index.html
@app.route("/")
def index():
    return flask.redirect('/static/index.html')


@app.route('/todos/<todoId>', methods=['DELETE'])
def del_todo(todoId):
    todos = Store.getInstance().todos
    newTodos = [t for t in todos if t['id'] != todoId]
    Store.getInstance().todos = newTodos
    return '', 204


@app.route('/todos/clear_completed', methods=['DELETE'])
def clear_completed():
    todos = Store.getInstance().all_todos
    todo = [t for t in todos if not t['completed']]
    return '', 204


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
    return '', 204


# add a new todo action


@app.route('/todos', methods=['POST'])
def add_todo():
    todos = Store.getInstance().todos
    fr = flask.request
    req = fr.get_json()
    todoStr = cleanStr(req['title'])
    if not todoStr:
        return '', 400
    todo = {
        "title": cleanStr(req['title']),
        "id": unsafeRandId(10),
        "completed": False
    }
    todos.append(todo)
    on_add_todo_logging(todoStr)
    return '', 204


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Store.getInstance().todos
    on_get_todos_logging(todos)
    return json.dumps(todos)


@app.route('/todo/dup/<todoId>', methods=['POST'])
def duplicate_todo(todoId):
    todos = Store.getInstance().todos
    for todo in todos:
        if todoId == todo['id']:
            dup = {'title': todo['completed'],
                   'id': unsafeRandId(10),
                   'completed': todo['title']}
            todos.append(dup)
            break
    return '', 204


@app.route('/todos/remove_all', methods=['DELETE'])
def remove_all():
    Store.getInstance().todos = []
    return '', 204


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'rookout_favicon.ico', mimetype='image/vnd.microsoft.icon')

def initialize_tracer():
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'local_agent': {
                'reporting_host': 'jaeger-agent',
                'reporting_port': 5775
            }
        },
        service_name='tutorial-python')
    return config.initialize_tracer()  # also sets opentracing.tracer


flask_tracer = FlaskTracer(initialize_tracer, True, app)

import rook
rook.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
