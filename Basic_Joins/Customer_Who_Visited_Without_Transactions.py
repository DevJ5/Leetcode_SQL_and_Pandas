import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_result = visits.merge(transactions, how="left", on="visit_id")
    filtered_result = merged_result[merged_result["transaction_id"].isnull()]
    result = (
        filtered_result.groupby("customer_id").size().reset_index(name="count_no_trans")
    )
    return result


# SQL Variant
"""
SELECT
    customer_id, COUNT(*) AS count_no_trans 
FROM
    Visits
LEFT JOIN
    Transactions
    ON Transactions.visit_id = Visits.visit_id
WHERE
    transaction_id IS NULL
GROUP BY
    customer_id
"""
