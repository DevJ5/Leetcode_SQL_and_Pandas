import pandas as pd


def confirmation_rate(
    signups: pd.DataFrame, confirmations: pd.DataFrame
) -> pd.DataFrame:
    merged = signups.merge(confirmations, how="left", on="user_id")

    # Create a boolean column: 1 if confirmed, else 0
    merged["is_confirmed"] = (merged["action"] == "confirmed").astype(int)

    # total actions per user_id
    total_actions = merged.groupby("user_id")["action"].count()
    # confirmed count per user_id
    confirmed_count = merged.groupby("user_id")["is_confirmed"].sum()

    # calculate rate
    confirmation_rate = (confirmed_count / total_actions).fillna(0).round(2)

    result = confirmation_rate.reset_index(name="confirmation_rate")
    return result


# SQL Variant
"""
SELECT 
    s.user_id, 
    ROUND(AVG(IF(c.action = "confirmed", 1, 0)), 2) AS confirmation_rate
FROM 
    Signups AS s
LEFT JOIN 
    Confirmations AS c
ON 
    s.user_id = c.user_id
GROUP BY 
    s.user_id;
"""
