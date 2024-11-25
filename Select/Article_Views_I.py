import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = views["author_id"] == views["viewer_id"]
    filtered_df = views.loc[mask, ["author_id"]].rename(columns={"author_id": "id"})
    distinct_ids = filtered_df.drop_duplicates()
    result = distinct_ids.sort_values(by="id", ascending=True).reset_index(drop=True)
    return result


# SQL Variant
"""SELECT DISTINCT
    author_id AS id
FROM
    Views
WHERE
    author_id = viewer_id
ORDER BY
    id ASC"""
