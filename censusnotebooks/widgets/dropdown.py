import ipywidgets as widgets
from IPython.display import display

class Dropdown:

    def __init__(self):
        """Initialize a Dropdown menu through user input."""
        self.options = []

        while True:
            option = input('Add an option to your dropdown box (or type \'stop\' if there are no more): ')
            if option == 'stop':
                break
            self.options.append(option)

        self.description = input('Enter the description of your dropdown box: ')

        dropdown = widgets.Dropdown(
        options=self.options,
        value=self.options[0],
        description=self.description
        )

        display(dropdown)
