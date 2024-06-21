import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, bonus, on="empId", how="left")
    df = df[(df["bonus"] < 1000) | df["bonus"].isnull()]
    df = df[["name", "bonus"]]
    return df


# select name, bonus
# from Employee e
# left join Bonus b on e.empId = b.empId
# where bonus < 1000 or bonus is null
