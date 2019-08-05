import ipywidgets as widgets
from IPython.display import display

class Text:

    def __init__(self):
        """Initializes a Text box through user input."""

        self.description = input('Enter the description of your Text box: ')

        textbox = widgets.Text(
            value='',
            placeholder='Type something',
            description=self.description,
            )

        display(textbox)

class Textarea:

    def __init__(self):
        """Initializes a Textarea (larger Text box) through user input."""

        self.description = input('Enter the description of your Text area: ')

        textarea = widgets.Textarea(
            value='',
            placeholder='Type something',
            description=self.description,
            )

        display(textarea)
