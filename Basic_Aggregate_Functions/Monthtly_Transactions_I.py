import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    transactions["is_approved"] = transactions["state"] == "approved"

    grouped = (
        transactions.groupby(["month", "country"])
        .agg(
            trans_count=("trans_date", "size"),
            approved_count=("is_approved", "sum"),
            trans_total_amount=("amount", "sum"),
        )
        .reset_index()
    )

    approved_amounts = (
        transactions[transactions["is_approved"]]
        .groupby(["month", "country"], dropna=False)["amount"]
        .sum()
        .reset_index()
        .rename(columns={"amount": "approved_total_amount"})
    )

    result = grouped.merge(approved_amounts, on=["month", "country"], how="left")
    result["approved_total_amount"] = result["approved_total_amount"].fillna(0)
    return result


# SQL Variant
"""
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(IF(state = "approved", 1, 0)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = "approved", amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
"""
