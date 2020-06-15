import os

from decorators import example


class DummyContext:
    def __init__(self, message="Lorem ipsum dolor sit amet..."):
        self.message = message

    def __enter__(self):
        print("Called __enter__")
        return self.message

    def __exit__(self, type, value, traceback):
        print("Called __exit__")


class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


@example.title(name="example_02")
def run():
    """Creating your own context manager via __enter__ and __exit methods"""

    with DummyContext() as context_object:
        print(f'context_object: { context_object }')

    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'demo.txt')

    with File(file_path, 'w') as opened_file:
        opened_file.write('Hola!\n')
        opened_file.write('Danke!\n')
