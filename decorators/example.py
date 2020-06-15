import os

def title(name, delimiter="="):
    def decorator(function):
        def print_banner(name, deliniter):
            print(delimiter * len(name))
            print(name.upper())
            print(delimiter * len(name), os.linesep)

        def wrapper(*args, **kwargs):
            print_banner(name, delimiter)
            value = function(*args, **kwargs)
            print(os.linesep)

            return value

        return wrapper

    return decorator
