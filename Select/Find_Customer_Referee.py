import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer["referee_id"] != 2) | (customer["referee_id"].isnull())
    result = customer.loc[mask, ["name"]]
    return result


# SQL Variant
"""
SELECT 
    name
FROM 
    Customer
WHERE
    referee_id <> 2
    OR referee_id IS NULL;
"""
