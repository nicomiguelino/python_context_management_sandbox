from contextlib import contextmanager
import os

from decorators import example


@contextmanager
def create_dummy_context(message='Lorem ipsum dolor sit amet...'):
    try:
        print("Called __enter__ equivalent")
        yield message
    finally:
        print("Called __exit__ equivalent")


@contextmanager
def open_file(file_path, method):
    file = open(file_path, method)
    try:
        yield file
    finally:
        file.close()


@example.title(name="example_03")
def run():
    """Implementing a context manager as a generator"""

    with create_dummy_context(
            "Some things are meant to be together.") as context_object:
        print(f'context_object: { context_object }')

    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'demo.txt')

    with open_file(file_path, 'w') as opened_file:
        opened_file.write('Hola!\n')
        opened_file.write('Danke!\n')
        opened_file.write('Merci!\n')
