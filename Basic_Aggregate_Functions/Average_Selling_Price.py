import pandas as pd


def average_selling_price(
    prices: pd.DataFrame, units_sold: pd.DataFrame
) -> pd.DataFrame:
    merged = prices.merge(units_sold, how="left", on="product_id")
    filtered = merged[
        merged["purchase_date"].between(merged["start_date"], merged["end_date"])
    ]
    grouped = filtered.groupby("product_id")
    temp = grouped.apply(lambda x: (x["units"] * x["price"]).sum() / x["units"].sum())
    result = temp.reset_index()
    result.columns = [result.columns[0], "average_price"]
    result["average_price"] = round(result["average_price"], 2).fillna(0)
    return result


# SQL Variant
"""
SELECT
    Prices.product_id,
    IFNULL(
        ROUND(SUM(units * price) / SUM(units), 2),
        0
    ) AS average_price
FROM
    Prices
LEFT JOIN
    UnitsSold
    ON UnitsSold.product_id = Prices.product_id
    AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
GROUP BY
    Prices.product_id;
"""
