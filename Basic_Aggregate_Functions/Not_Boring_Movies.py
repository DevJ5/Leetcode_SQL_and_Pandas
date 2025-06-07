import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[
        (cinema["description"].str.lower() != "boring") & (cinema["id"] % 2 == 1)
    ]
    cinema = cinema.sort_values(by="rating", ascending=False)
    return cinema


# SQL Variant
"""
SELECT
    *
FROM
    Cinema
WHERE
    LOWER(description) <> 'boring'
    AND id % 2 = 1
ORDER BY
    rating DESC;
"""
