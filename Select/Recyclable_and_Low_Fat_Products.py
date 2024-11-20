import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    subset = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return subset[["product_id"]]


# SQL Variant
"""
SELECT
    product_id
FROM
    Products
WHERE low_fats = 'Y'
    AND recyclable = 'Y';
"""
