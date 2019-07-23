import ipywidgets as widgets

class RadioButton:

    def __init__(self):
        """Initialize a RadioButton through user input."""

        self.options = []
        while True:
            option = input('Add an option to your RadioButton (or type \'stop\' if there are no more): ')
            if option == 'stop':
                break
            self.options.append(option)

        self.description = input('Enter the description of your RadioButton: ')
        return widgets.RadioButton(
        options=self.options,
        description=self.description
        )
