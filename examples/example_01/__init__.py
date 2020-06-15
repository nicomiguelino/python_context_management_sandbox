import os

from decorators import example


@example.title(name="example_01")
def run():
    """Using built-in context manager for files."""
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'some_file.txt')

    with open(file_path, 'w') as opened_file:
        opened_file.write('Hola!')

    print(f'The file has been written to: { file_path }')

    # But is it possible to create your own context manager?
