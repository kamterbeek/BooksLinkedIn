import pandas as pd

def clean_value(value):
    """
    Convert Pandas NaN values into Python None.
    """
    if pd.isna(value):
        return None
    return value

def clean_isbn(value):
    """Remove Goodreads Excel Formatting from ISBN values."""
    value = clean_value(value)

    if value is None:
        return None