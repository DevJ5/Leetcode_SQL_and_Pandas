import pandas as pd


def average_selling_price(
    prices: pd.DataFrame, units_sold: pd.DataFrame
) -> pd.DataFrame:
    merged = prices.merge(
        units_sold, how="left", on="product_id", suffixes=("", "_sold")
    )
    filtered = merged[
        merged["purchase_date"].between(merged["start_date"], merged["end_date"])
    ].copy()

    filtered["revenue"] = filtered["units"] * filtered["price"]

    grouped = filtered.groupby("product_id", as_index=False).agg(
        {"revenue": "sum", "units": "sum"}
    )

    grouped["average_price"] = (grouped["revenue"] / grouped["units"]).round(2)
    grouped["average_price"] = grouped["average_price"].fillna(0)

    result = (
        prices[["product_id"]]
        .drop_duplicates()
        .merge(grouped[["product_id", "average_price"]], on="product_id", how="left")
    )
    result["average_price"] = result["average_price"].fillna(0)

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
