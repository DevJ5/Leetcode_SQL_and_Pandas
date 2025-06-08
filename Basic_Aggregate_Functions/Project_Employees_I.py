import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, on="employee_id", how="left")
    result = merged.groupby("project_id", as_index=False).agg(
        average_years=("experience_years", "mean")
    )
    result["average_years"] = result["average_years"].round(2)
    return result


# SQL Variant
"""
SELECT
    project_id, ROUND(AVG(experience_years), 2) AS average_years
FROM
    Project
LEFT JOIN
    Employee
    ON Project.employee_id = Employee.employee_id
GROUP BY
    project_id
ORDER BY
    project_id ASC;
"""
