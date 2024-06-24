import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[
        (cinema["description"].str.lower() != "boring") & (cinema["id"] % 2 == 1)
    ]
    cinema = cinema.sort_values(by="rating", ascending=False)
    return cinema


# select *
# from Cinema
# where LOWER(description) <> 'boring' and id % 2 = 1
# order by rating desc
