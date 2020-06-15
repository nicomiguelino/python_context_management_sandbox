import os

from decorators import example


class Indenter:
    def __init__(self, tab_width=4):
        self.level = 0
        self.tab_width = tab_width

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, type, value, traceback):
        self.level -= 1

    def print(self, text):
        indent = ' ' * self.tab_width * self.level
        print(indent + text)


@example.title(name="example_04")
def run():
    """A non-file example of using context manager in your code"""

    with Indenter() as indenter:
        indenter.print('Thank you!')
        with indenter:
            indenter.print('Danke!')
            with indenter:
                indenter.print('Merci')
                with indenter:
                    indenter.print('Salamat')
            indenter.print('Gracias')

        indenter.print('Tak')
