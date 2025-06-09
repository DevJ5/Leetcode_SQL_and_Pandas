def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = users["user_id"].nunique()
    grouped = (
        register.groupby("contest_id")["user_id"]
        .nunique()
        .div(total_users)
        .mul(100)
        .round(2)
        .reset_index()
    )
    result = grouped.rename(columns={"user_id": "percentage"})
    result.sort_values(
        by=["percentage", "contest_id"], ascending=[False, True], inplace=True
    )
    return result


# SQL Variant
"""
SELECT
  contest_id,
  ROUND(
    COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(user_id) FROM Users),
    2
  ) AS percentage
FROM
  Register
GROUP BY
  contest_id
ORDER BY
  percentage DESC,
  contest_id;
"""
