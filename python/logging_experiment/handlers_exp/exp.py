import logging
from my_logger import what_is_my_name as _what_is_my_name
from my_logger import my_handler

# The following will show that __name__ inside a function
# will get the name of the module where the function
# is sitting in
print(_what_is_my_name())

# create logger
logger = logging.getLogger(__name__)
handler = my_handler()
logger.addHandler(handler)


def test_logger():
    """
    test_logger tests the logger by running though
    all the logging levels
    """
    logger.info('info message')
    logger.critical('critical message')
    logger.debug('debug message')
    logger.warning('warning message')
    logger.error('error message')


if __name__ == "__main__":
    test_logger()
