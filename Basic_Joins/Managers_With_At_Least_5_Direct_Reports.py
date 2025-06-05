import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        employee,
        employee["managerId"].value_counts(),
        how="left",
        left_on="id",
        right_on="managerId",
    )
    filtered = merged[merged["count"] >= 5]
    return filtered[["name"]]


# SQL Variant
"""
SELECT NAME
FROM   employee
WHERE  id IN (SELECT managerid
              FROM   employee
              GROUP  BY managerid
              HAVING Count(*) >= 5)
"""
