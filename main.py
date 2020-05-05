import logging
import os
import sys
from logging import Formatter

import coloredlogs


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

coloredlogs.install()


if __name__ == "__main__":
    logger.debug("Python main handler got invoked!")
    logger.info(f"Starting ${os.environ.get('GITHUB_REPOSITORY')}-${os.environ.get('GITHUB_WORKFLOW')}:${os.environ.get('GITHUB_ACTION')}")

    logger.info(os.environ)
    logger.warning(sys.argv)
