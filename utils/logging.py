import logging
import flask

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def on_add_todo_logging(todoStr):
    logger.info("Successfully added a new task to do")
    logger.debug(' ---- request http headers: ----')
    for header in flask.request.headers:
        logger.debug(header)
    logger.debug("The user needs to do - @@@@@@@@ %s @@@@@@@@" % todoStr)
    logger.debug("add_todo() function works")

    if not todoStr.replace(" ", "").isalnum():
        logger.error("The user added a non-alphanumeric character to his task !!!")
        logger.debug("make sure your user is not a robot")


def on_get_todos_logging(todos):
    logger.info("fetched the user's todo tasks")
    logger.debug(' ---- request http headers: ----')
    for header in flask.request.headers:
        logger.debug(header)
    logger.debug("get_todos() function works")

    logger.debug(' ---- all todos: ----')
    for todo in todos:
        status = "completed" if todo["completed"] else "uncompleted"
        logger.debug("%s --- %s" % (todo['title'],status))

    if len(todos) == 0:
        logger.warning("The user has no tasks to do yet")
        logger.debug("Make sure to tell the user he can add todos")
    elif len(todos) > 5:
        logger.critical("The user has more than 5 tasks to do !!!!")
        logger.debug("Tell the user to plan his time wisely")

