import pandas as pd


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    sorted_df = delivery.sort_values(
        ["customer_id", "order_date"], ascending=[True, True]
    )
    grouped = sorted_df.groupby(["customer_id"]).head(1)
    immediate_percentage = len(
        grouped[grouped["order_date"] == grouped["customer_pref_delivery_date"]]
    ) / len(grouped)
    return pd.DataFrame(
        {"immediate_percentage": [round(immediate_percentage * 100, 2)]}
    )


# SQL Variant
"""
SELECT
    ROUND(AVG(IF(order_date = customer_pref_delivery_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM
    Delivery d
WHERE
    (customer_id, order_date) IN (
        SELECT
            customer_id,
            MIN(order_date) AS first_order_date
        FROM
            Delivery
        GROUP BY
            customer_id
    );
"""
