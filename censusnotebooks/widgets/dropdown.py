import ipywidgets as widgets

class Dropdown:

    def __init__(self):
        """Initialize a Dropdown menu through user input."""
        self.options = []

        while True:
            option = input('Add an option to your dropdown box (or type \'stop\' if there are no more): ')
            if option == 'stop':
                break
            self.options.append(option)

        self.value = input('Enter your starting value of your dropdown box: ')
        self.description = input('Enter the description of your dropdown box: ')

        dropdown = widgets.Dropdown(
        options=self.options,
        value=self.value,
        description=self.description
        )

        display(dropdown)
