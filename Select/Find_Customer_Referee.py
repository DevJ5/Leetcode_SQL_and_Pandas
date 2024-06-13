import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    subset = customer[(customer["referee_id"] != 2) | (customer["referee_id"].isnull())]
    return subset[["name"]]


# select name from Customer
# where referee_id <> 2 or referee_id IS NULL;
