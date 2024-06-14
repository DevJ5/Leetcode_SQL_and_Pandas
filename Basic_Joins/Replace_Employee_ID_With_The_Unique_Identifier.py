import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    df = pd.merge(employees, employee_uni, how="left", on="id")
    return df[["unique_id", "name"]]


# select unique_id, name
# from Employees
# left join EmployeeUNI on Employees.id = EmployeeUNI.id
