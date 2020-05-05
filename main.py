import logging
import os
import sys
from logging import Formatter


class LogFormatter(Formatter):
    def format(self, record):
        log_level = record.levelname
        location = f"{record.module}.{record.funcName}:{record.lineno}"
        message = super().format(record)

        log = f"[{log_level}] " f"{location}: {message}"
        return log

handler = logging.StreamHandler()
handler.setFormatter(LogFormatter())

logger = logging.getLogger("PyCICD")
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))
logger.addHandler(handler)

def invoke_handler():
    logger.info(sys.argv)
    command = sys.argv[1]

    args = []
    if len(sys.argv) > 2:
        args = sys.argv[2:]

    logger.debug(f"Invoking command={command} with args={args}")


if __name__ == "__main__":
    logger.debug("Python main handler got invoked!")
    logger.info(f"Starting {os.environ.get('GITHUB_REPOSITORY')}-{os.environ.get('GITHUB_WORKFLOW')}:{os.environ.get('GITHUB_ACTION')}")

    # TODO: remove this
    logger.info(os.environ)

    try:
        invoke_handler()
    except Exception as e:
        logger.error(f"Failed to run this job! ex={e}")
        sys.exit(-1)
