import logging

def _get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.WARN)

    # Create a handler that writes log messages to the console
    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARN)

        # Create a formatter and set it for the handler
        formatter = logging.Formatter('%(levelname)s:  %(message)s')
        console_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(console_handler)
    return logger