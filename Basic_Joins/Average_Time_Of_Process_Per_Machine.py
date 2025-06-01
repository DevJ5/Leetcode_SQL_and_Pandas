import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        activity,
        activity,
        on=["machine_id", "process_id"],
        suffixes=("_left", "_right"),
    )

    df = df[
        (df["activity_type_left"] == "start") & (df["activity_type_right"] == "end")
    ]

    df["processing_time"] = df["timestamp_right"] - df["timestamp_left"]

    grouped = (
        df.groupby("machine_id", as_index=False)["processing_time"].mean().round(3)
    )
    # grouped = df.groupby('machine_id')['processing_time'].mean().round(3).reset_index()

    return grouped


# SQL Variant
"""
SELECT a1.machine_id,
       Round(Avg(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM   activity a1
       JOIN activity a2
         ON a1.machine_id = a2.machine_id
            AND a1.process_id = a2.process_id
WHERE  a1.activity_type = 'start'
       AND a2.activity_type = 'end'
GROUP  BY a1.machine_id;
"""
