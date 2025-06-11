import pandas as pd


class FeatureEngineering:
    """
    A class to create feature engineering from the data of a pandas DataFrame with different functions.
    """

    def __init__(self, data):
        """
        Initialize the class with a DataFrame.

        Args:
                        data (pd.DataFrame): The DataFrame containing the data to process
        """
        self.data = data

    def convert_date_column(self, col_name="InvoiceDate", date_format="%d-%m-%Y"):
        """
        Converts a date column in the DataFrame to datetime objects.

        Args:
                        col_name (str): Name of the column to convert. Default to 'InvoiceDate'.
                        date_format (str): Format of the input dates. Default to "%d-%m-%Y".
        """
        self.data[col_name] = pd.to_datetime(self.data[col_name], format=date_format)

    def extract_year_and_month_column(
        self, col_name="InvoiceDate", month_col="Month", year_col="Year"
    ):
        """
        Extract the year and the month from a column in the DataFrame

        Args:
                col_name (str, optional): Name of the column which it will extract the month. Defaults to "InvoiceDate".
        """
        self.data[year_col] = pd.DatetimeIndex(self.data[col_name]).year
        self.data[month_col] = pd.DatetimeIndex(self.data[col_name]).month

    def add_season_column(self, month_col="Month", season_col="Season"):
        """
        Adds a season column based on month numbers (1-12).

        Args:
                        month_col (str): Name of the column containing month numbers. Default to 'Month'.
                        season_col (str): Name of the new season column to create. Default to 'Season'.
        """
        month_to_season = {
            1: "Winter",
            2: "Winter",
            3: "Spring",
            4: "Spring",
            5: "Spring",
            6: "Summer",
            7: "Summer",
            8: "Summer",
            9: "Fall",
            10: "Fall",
            11: "Fall",
            12: "Winter",
        }

        self.data[season_col] = self.data[month_col].map(month_to_season)

    @staticmethod
    def extract_am_pm(time):
        """
        Takes the time as a string and extracts if it's AM or PM
        Args:
                        time (str): time as a string
        return:
                        AM or PM
        """
        am_pm = time.split()[1]
        return am_pm
