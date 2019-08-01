import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

### Utilities ###
types = ['histogram', 'barplot', 'scatterplot', 'lineplot']

class Plot():

    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise ValueError('Your data must be a table (Pandas DataFrame). Please try again. \n')

        self.data = data
        self.type = None
        self.arg = None
        self.arg2 = None
        self.xlab = None
        self.ylab = None
        self.title = None
        self.ax = None

    def ask_type(self):
        
        ## we can use the drop down menu here to simply it.
        print('Here are the types of plots you may use: \n')
        for t in types:
            print(f'({types.index(t) + 1}) {t} \n')

        type_holder = input("Enter the number associated to the type of plot you would like to use: \n")

        while type_holder not in [str(x) for x in list(np.arange(1, len(types)+1))]:
            print('** ERROR: You must enter the numbers listed above. ** \n')
            type_holder = input("Enter the number associated to the type of plot you would like to use: \n")

        self.type = types[int(type_holder) - 1]
        print(f"Plotting a {self.type}.")


    def ask_columns(self):
        if self.type == 'histogram' :
            arg_max = 1
        else:
            arg_max = 2

        columns = list(self.data.columns)

        print('Here are the columns of your table:')
        for c in columns:
            print(f'({columns.index(c) + 1}) {c} \n')

        column_holder1 = input("Enter the column you would like to plot: \n")

        while column_holder1 not in [str(x) for x in list(np.arange(1, len(columns)+1))]:
            print('** ERROR: You must enter the numbers listed above. ** \n')
            column_holder1 = input("Enter the column you would like to plot: \n")

        self.arg = columns[int(column_holder1) - 1]

        if arg_max == 1:
            print(f'You are plotting {self.arg} only. \n')
        else:
            column_holder2 = input("Enter the second column you would like to plot: \n")

            while column_holder2 not in [str(x) for x in list(np.arange(1, len(columns)+1))]:
                print('** ERROR: You must enter the numbers listed above. ** \n')
                column_holder2 = input("Enter the column you would like to plot: \n")

            self.arg2 = columns[int(column_holder2) - 1]
            print(f'You are plotting {self.arg} and {self.arg2}. \n')


    def ask_labels(self):
        self.xlab = input("Enter the x-axis label for your plot: \n")
        self.ylab = input("Enter the y-axis label for your plot: \n")
        self.title = input("Enter the title for your plot: \n")


    def ask_figure_size(self):
        ### Add this in later
        return None


    def plotting(self):
        if self.type == 'histogram':
            self.ax = sns.distplot(a=self.data.loc[:, self.arg], kde=False);

        elif self.type == 'barplot':
            self.ax = sns.barplot(x=self.arg, y=self.arg2, data=self.data);

        elif self.type == 'scatterplot':
            self.ax = sns.scatterplot(x=self.arg, y=self.arg2, data=self.data);

        elif self.type == 'lineplot':
            self.ax = sns.lineplot(x=self.arg, y=self.arg2, data=self.data);

    def labeling(self):
        self.ax.set(title=self.title,
                    xlabel=self.xlab,
                    ylabel=self.ylab
                    )

        plt.show();


    def new_plot(self):
        self.ask_type()
        self.ask_columns()
        self.ask_labels()
        self.plotting()
        self.labeling()
