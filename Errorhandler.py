import typing
import sys


# decorator exception handling
def error(function: typing.callable):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(f'Function <{function.__name__}> encountered an exception: {sys.exc_info()[0], sys.exc_info()[1]}')
    return wrapper            