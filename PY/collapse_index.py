import pandas as pd

def collapse_index(list_in: list) -> pd.DataFrame:
    """
    Collapse Index
    A function for converting a list of dataframes into a row-stacked dataframe.
    
    :param list_in: A list of pandas DataFrames.
    :return: A single pandas DataFrame with all input DataFrames stacked.
    """
    if not list_in:
        return pd.DataFrame()
    
    return pd.concat(list_in, ignore_index=True)