#!/usr/bin/env python3

class Log(object):
    """ Class for writing logs in file"""

    def __init__(self, name):
        """ Saves the name into self._name """
        self._name = name

    def __enter__(self):
        """ Open file and write Begin to the log file """
        self._file = open(self._name, "w")
        self._file.write("Begin\n")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Finish writing to the file and closed it """
        self._file.write("End\n")
        self._file.close()

    def logging(self, text):
        """ Read the text and write it to the log """
        one_log = text + "\n"
        self._file.write(one_log)

def ordered_merge(*args, **kwargs):
    """ Generator depended on the selector """

    if kwargs == {}:
        return []

    selector = kwargs["selector"]

    iterations = [iter(i) for i in args]
    for x in selector:
        yield next(iterations[x])

class TooManyCallsError(Exception):
    """ exception for the limit_calls """
    def __call__(self, *args, **kwargs):
        """ exception is raised if this class is called """
        Exception.__init__(self, *args, **kwargs)

def limit_calls(max_calls=2, message="called too often"):
    """ function that remebers how many times function has been called """

    def decorator(func):
        # all arguments are loaded into variables
        func.calls_max = max_calls
        func.calls_message = message
        func.calls_amount = 0
        def wrapper(*args, **kwargs):
            # amount of call is incremented
            func.calls_amount = func.calls_amount + 1
            # content of error is prepared
            content = "function \"{}\" - {}".format(func.__name__, func.calls_message);
            # check whether error should be raised
            if func.calls_amount > func.calls_max:
                raise TooManyCallsError(content)
            return func(*args, **kwargs)
        return wrapper
    return decorator
