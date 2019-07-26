import ipywidgets as widgets

class Slider:

    def __init__(self, description = '', start=0, min=0, max=10, step=1, orientation='horizontal'):
        """Initialize a Slider through user input.

        Keyword arguments:
        description -- description of slider (default '')
        start -- starting value(s) of slider; either a single number or a list representing a range (default 0)
        min -- minimum value of slider (default 0)
        max -- maximum value of slider (default 10)
        step -- step size of slider (default 1)
        orientation -- orientation of slider; either 'horizontal' or 'vertical' (default 'horizontal')
        """
        self.description = input("Enter the description of your slider: ")
        self.start = input("Enter the starting value(s) of your slider (if multiple, no commas between values!): ")
        self.min = int(input("Enter the minimum value of your slider: "))
        self.max = int(input("Enter the maximum value of your slider: "))
        self.step = int(input("Enter the step size of your slider: "))
        self.orientation = input("Horizontal or vertical orientation?: ").lower()
        self.slider_type = 'integer'

        if len(self.start.split()) > 1:
            self.start = [num for num in self.start.split()]
            self.slider_type = 'integerRange'

            for num in self.start:
                if len(num) > 1:
                    num = float(num)
                    self.slider_type = 'decimalRange'
                else:
                    num = int(num)
        else:
            if len(self.start) > 1:
                self.start = float(self.start)
                self.slider_type = 'decimal'
            else:
                self.start = int(self.start)

        slider = self.showSlider()
        display(slider)

    def showSlider(self):
        """Return this slider according to appropriate slider type. Used in __init__."""
        if self.slider_type == 'integer':
            return self.integer()
        if self.slider_type == 'decimal':
            return self.decimal()
        if self.slider_type == 'integerRange':
            return self.integerRange()
        return self.decimalRange()

    def integer(self):
        """Return an IntSlider."""
        return widgets.IntSlider(
        value=self.start,
        min=self.min,
        max=self.max,
        step=self.step,
        description=self.description,
        orientation=self.orientation
        )

    def decimal(self):
        """Return a FloatSlider."""
        return widgets.FloatSlider(
        value=self.start,
        min=self.min,
        max=self.max,
        step=self.step,
        description=self.description,
        orientation=self.orientation
        )

    def integerRange(self):
        """Return a IntRangeSlider."""
        return widgets.IntRangeSlider(
        value=self.start,
        min=self.min,
        max=self.max,
        step=self.step,
        description=self.description,
        orientation=self.orientation
        )

    def decimalRange(self):
        """Return a FloatRangeSlider."""
        return widgets.FloatRangeSlider(
        value=self.start,
        min=self.min,
        max=self.max,
        step=self.step,
        description=self.description,
        orientation=self.orientation
        )
