import flask
import re
import string
import random
import json
from datetime import datetime
from random import randint
from todos_store import Store
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from jaeger_client import Config
from flask_opentracing import FlaskTracer

sentry_sdk.init(
    dsn="https://2acefaf842814814848afd40457bc55d@sentry.io/1381062",
    integrations=[FlaskIntegration()]
)

app = flask.Flask(__name__, static_url_path='/static')


# unsafeRandId generates a random string composed from english upper case letters and digits
# it's called unsafe because it doesn't use a crypto random generator
def unsafeRandId(len):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len))


def cleanStr(str):
    return re.sub(r'[>|<|;|`|&|/|\\]', '', str)


@app.errorhandler(404)
def page_not_found(e):
    return '404 Page Not Found'


@app.errorhandler(500)
def internal_server_error(e):
    return '500 Internal Server Error'


@app.route("/error")
def render_bad_template():
    try:
        invalid_oper = 42 / 0
    except Exception as e:
        print('Operation failed to complete')
    animal_list = ['dog', 'cat', 'turtle', 'fish', 'bird', 'cow', 'sealion']
    time = datetime.now()
    number = 0.01 * randint(10, 200) + 0.1
    return flask.render_template('doesnotexist.html', animal_list=animal_list, time=time, number=number)


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
    todos = Store.getInstance().todos
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
    return '', 204


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Store.getInstance().todos
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
