import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sales, product, on="product_id", how="inner")
    return df[["product_name", "year", "price"]]


# select product_name, year, price
# from Sales
# inner join Product on Sales.product_id = Product.product_id
