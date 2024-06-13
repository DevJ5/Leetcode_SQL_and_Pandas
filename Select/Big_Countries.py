import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    subset = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    return subset[["name", "population", "area"]]


# select name,population,area from World
# where area >= 3000000 or population >= 25000000
