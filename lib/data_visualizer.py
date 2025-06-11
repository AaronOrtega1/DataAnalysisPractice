import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


class DataVisualizer:
    """
    A class to visualize data from a pandas DataFrame with different functions.
    """

    def __init__(self, data):
        """
        Initialize the class with a DataFrame.

        Args:
                data (pd.DataFrame): The DataFrame contains the data to visualize
        """
        self.data = data

    def plot_heatmap(self, title="", annot=True, cmap="coolwarm"):
        """
        Create a heatmap of the correlational matrix of the DataFrame.

        Args:
                title (str, optional): Title for the heatmap. Defaults to "".
                annot (bool, optional): Wether to put annotations in the matrix. Defaults to True.
                color (str, optional): color schema for the heatmap. Defaults to "coolwarm".
        """
        try:
            numeric_df = self.data.select_dtypes(include=["float64", "int64"])
            plt.figure(figsize=(12, 8))
            sns.heatmap(numeric_df.corr(), annot=annot, cmap=cmap)
            plt.title(title)
            plt.show()
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def number_of_unique(self):
        """
        Prints the num of unique values for each column of the a DataFrame.
        """
        for col in self.data.columns:
            print(
                f"{col} Column has {self.data[col].nunique()} number of unique values."
            )

    def barplot_percentage(self, column, title="", slice=12, log_scale=False):
        """
        Creates a bar plot with percentage labels for a categorical column.

        Args:
                column (str): Column that will be taken to plot.
                title (str, optional): Title of the plot. Defaults to "".
                slice (int, optional): Number of top categories to diplay. Defaults to 12.
                log_scale (boolean, optional): Wether to use a logarithmic scale for the y-axis. Defaults to False.

        Raises:
                ValueError: If the column is not in the DataFrame columns
        """
        try:
            if column not in self.data.columns:
                raise ValueError(f"Column '{column}' not found in the DataFrame.")

            # number of rows
            total = self.data.shape[0]

            fig, axix = plt.subplots(figsize=(14, 8))
            axis = sns.barplot(self.data[column].value_counts()[:slice])
            axis.set_title(title)

            # Adding percentage to the bars
            for p in axis.patches:
                width = p.get_width()
                height = (
                    p.get_height()
                )  # the height is equal to the total of occurences
                percentage = f"{100 * height / total:.1f}%"
                x, y = (
                    p.get_xy()
                )  # gets the coordinates of the bottom left corner of the bar
                axis.annotate(
                    f"{percentage}", (x + width / 2, y + height * 1.02), ha="center"
                )  # put the annotation at the center a little bit above the top of the bar.

            plt.ylabel("Count")

            if log_scale:
                plt.yscale("log")

            plt.show()

        except Exception as e:
            print(f"An error ocurred: {e}")

    def oldest_latest_date(self, column):
        """
        Gets the latest and oldest data from a specific column from a DataFrame.

        Args:
                column (str): column to find the lastest and oaxldest data

        Raises:
                ValueError: Error if column is not in the columns of the DataFrame.
        """
        try:
            if column not in self.data.columns:
                raise ValueError(f"Column '{column}' not found in the DataFrame.")

            print(
                f"The oldest date is: {self.data[column].min()}, while the latest date is: {self.data[column].max()}"
            )

        except Exception as e:
            print(f"An error ocurred: {e}")
