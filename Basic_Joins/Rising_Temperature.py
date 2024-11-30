import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    pd.set_option("display.max_columns", None)
    weather["yesterday"] = weather["recordDate"] - pd.Timedelta(days=1)
    merged = weather.merge(
        weather,
        how="inner",
        left_on="yesterday",
        right_on="recordDate",
        suffixes=("_x", "_y"),
    )
    filtered = merged[merged["temperature_x"] > merged["temperature_y"]]
    result = filtered[["id_x"]].rename(columns={"id_x": "id"})
    return result


# SQL Variant
"""
SELECT 
    t1.id
FROM
    Weather t1
JOIN
    Weather t2
    ON t1.recordDate = DATE_ADD(t2.recordDate, INTERVAL 1 DAY)
WHERE
    t1.temperature > t2.temperature
"""
