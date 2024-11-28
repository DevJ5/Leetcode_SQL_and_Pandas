import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_result = sales.merge(product, how="left", on="product_id")
    return merged_result[["product_name", "year", "price"]]


# SQL Variant
"""
SELECT
    product_name, year, price
FROM
    Sales
LEFT JOIN
    Product 
    ON Sales.product_id = Product.product_id
"""
