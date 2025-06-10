import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    #
    queries["quality"] = queries.rating / queries.position + 1e-6
    queries["poor_query_percentage"] = (queries.rating < 3) * 100
    grouped = (
        queries.groupby("query_name")
        .agg({"quality": "mean", "poor_query_percentage": "mean"})
        .round(2)
    )
    return grouped.reset_index()


# SQL Variant
"""
SELECT
    query_name,
    ROUND(AVG(rating * 1.0 / position), 2) AS quality,
    ROUND(
        AVG(CASE
                WHEN rating < 3 THEN 1
                ELSE 0
            END) * 100,
        2
    ) AS poor_query_percentage
FROM
    Queries
WHERE
    query_name IS NOT NULL
GROUP BY
    query_name;
"""
