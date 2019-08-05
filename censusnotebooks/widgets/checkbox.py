import ipywidgets as widgets
from IPython.display import display

class Checkbox:

    def __init__(self):
        """Initializes a Checkbox through user input."""

        self.description = input('Enter the description for your Checkbox: ')
        checkbox = widgets.Checkbox(description=self.description)

        display(checkbox)
