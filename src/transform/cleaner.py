import pandas as pd


def clean_value(value):
    """Convert Pandas NaN values to None."""
    if pd.isna(value):
        return None
    return value


def clean_isbn(value):
    """Remove Goodreads Excel formatting from ISBN values."""
    value = clean_value(value)

    if value is None:
        return None

    return str(value).replace('="', "").replace('"', "")


def clean_int(value):
    """Convert numeric values to integers where possible."""
    value = clean_value(value)

    if value is None:
        return None

    return int(value)
        return None