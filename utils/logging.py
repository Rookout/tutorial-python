import logging

logger = logging.getLogger(__name__)


def on_add_todo_logging():
    logger.info("success")


def on_get_todos_logging():
    logger.error("oopsi")
