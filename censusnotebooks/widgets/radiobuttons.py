import ipywidgets as widgets
from IPython.display import display

class RadioButton:

    def __init__(self):
        """Initialize a RadioButton through user input."""

        self.options = []
        while True:
            option = input('Add an option to your RadioButton (or type \'stop\' if there are no more): ')
            if option.lower() == 'stop':
                break
            self.options.append(option)

        self.description = input('Enter the description of your RadioButton: ')

        radio_button = widgets.RadioButtons(
                    options=self.options,
                    description=self.description
                    )

        display(radio_button)
