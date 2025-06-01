import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, bonus, on="empId", how="left")
    df = df[(df["bonus"] < 1000) | df["bonus"].isnull()]
    df = df[["name", "bonus"]]
    return df


# SQL Variant
"""
SELECT NAME,
       bonus
FROM   employee e
       LEFT JOIN bonus b
              ON e.empid = b.empid
WHERE  bonus < 1000
        OR bonus IS NULL  
"""
