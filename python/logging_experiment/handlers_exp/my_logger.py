import logging


def what_is_my_name():
    """This function will prove that __name__
    is only for the module where this function is from
    """
    return __name__


def my_handler(level=None):
    """
    my_handler creates a logging handler

    :param level: level of the logging, defaults to None
    :type level: logging level obj such as logging.DEBUG, optional
    :return: a handler for logger
    """
    if level is None:
        level = logging.DEBUG
    handler = logging.StreamHandler()

    # formatter_simple = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    formatter_function_name = logging.Formatter("[%(asctime)s - %(name)s - %(levelname)s (%(funcName)s()@%(filename)s:%(lineno)s):: %(message)s")
    handler.setFormatter(formatter_function_name)
    handler.setLevel(level)

    return handler
