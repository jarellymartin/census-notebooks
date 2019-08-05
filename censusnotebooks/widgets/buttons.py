import ipywidgets as widgets
from IPython.display import display

class Buttons:

    def __init__(self):
        """Initialize a set of Buttons through user input."""

        self.options = []
        while True:
            option = input('Add an option to your set of buttons (or type \'stop\' if there are no more): ')
            if option.lower() == 'stop':
                break
            self.options.append(option)

        self.description = input('Enter the description of your set of buttons: ')

        buttons = widgets.ToggleButtons(
                options=self.options,
                description=self.description,
                button_style='info'
                )

        display(buttons)
