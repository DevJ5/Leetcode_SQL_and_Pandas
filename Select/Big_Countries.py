import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    mask = (world["population"] >= 25000000) | (world["area"] >= 3000000)
    result = world.loc[mask, ["name", "population", "area"]]
    return result


# SQL Variant
"""
SELECT
    name, population, area
FROM
    World
WHERE
    population >= 25000000
    OR area >= 3000000
"""
