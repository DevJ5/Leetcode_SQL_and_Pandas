import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    subset = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return subset[["product_id"]]


# select product_id from Products where low_fats = 'Y' and recyclable = 'Y';
