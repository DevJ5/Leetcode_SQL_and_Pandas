import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate"] = pd.to_datetime(weather["recordDate"])
    weather_shifted = weather.copy()
    weather_shifted["recordDate"] = weather_shifted["recordDate"] + pd.to_timedelta(
        1, unit="D"
    )
    merged_df = pd.merge(
        weather, weather_shifted, on="recordDate", suffixes=("_today", "_yesterday")
    )
    result = merged_df[
        merged_df["temperature_today"] > merged_df["temperature_yesterday"]
    ]
    result = result[["id_today"]].rename(columns={"id_today": "Id"})
    return result


# SELECT t1.id
# FROM Weather t1
# JOIN Weather t2
# ON t1.recordDate = t2.recordDate + INTERVAL 1 DAY
# WHERE t1.temperature > t2.temperature
