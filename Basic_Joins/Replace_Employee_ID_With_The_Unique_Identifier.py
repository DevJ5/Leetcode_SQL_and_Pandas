import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    merged_result = employees.merge(employee_uni, how="left", on="id")
    result = merged_result[["unique_id", "name"]]
    return result


# SQL Variant
"""
SELECT
    unique_id, name
FROM 
    Employees
LEFT JOIN
    EmployeeUNI ON Employees.id = EmployeeUNI.id
"""
