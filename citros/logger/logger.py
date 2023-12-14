import sys
import logging
from rich.logging import RichHandler
from rich import print, inspect, print_json
from logging.handlers import TimedRotatingFileHandler


FORMATTER = logging.Formatter(
    "[%(asctime)s] [%(name)s.%(funcName)s:%(lineno)d] [%(levelname)s]: %(message)s"
)


def get_rich_hangler():
    handler = RichHandler(rich_tracebacks=True)
    handler.setFormatter(FORMATTER)
    return RichHandler(rich_tracebacks=True)


# log to console
def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


# log to file
def get_file_handler(log_file):
    file_handler = TimedRotatingFileHandler(log_file, when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def str_to_log_level(level: str):
    if level == "debug" or level == "DEBUG":
        return logging.DEBUG
    elif level == "info" or level == "INFO":
        return logging.INFO
    elif level == "warn" or level == "WARN":
        return logging.WARNING
    elif level == "error" or level == "ERROR":
        return logging.ERROR
    else:
        # default to debug on invalid input
        return logging.INFO


def get_logger(
    logger_name,
    log_level="info",
    log_file=".citros/logs/citros.log",
):
    logger = logging.getLogger(logger_name)
    logger.setLevel(str_to_log_level(log_level))

    file_handler = get_file_handler(log_file)
    logger.addHandler(file_handler)

    # write to console when debugging
    if log_level == "debug":
        # logger.addHandler(get_console_handler())
        logger.addHandler(get_rich_hangler())

    return logger


def shutdown_log():
    logging.shutdown()
