import logging
import flask

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def on_add_todo_logging(todoStr):
    logger.info(flask.request.headers)
    logger.info("Successfully added a new task to do")
    logger.info(f"The user needs to do - {todoStr}")
    logger.debug("add_todo() function works")

    if not todoStr.isalnum():
        logger.error("The user added a non-alphanumeric character to his task !!!")
        logger.debug("make sure your user is not a robot")


def on_get_todos_logging(todos):
    logger.info(flask.request.headers)
    logger.info("fetched the user's todo tasks")
    logger.debug("get_todos() function works")

    if len(todos) == 0:
        logger.warning("The user have no tasks to do yet")
        logger.debug("Make sure to tell the user he can add todos")
    elif len(todos) > 5:
        logger.critical("The user has more than 5 tasks to do !!!!")
        logger.debug("Tell the user to plan his time wisely")

