import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets["content"].str.len() > 15
    return tweets.loc[mask, ["tweet_id"]]


# SQL Variant
"""
SELECT
    tweet_id
FROM
    Tweets
WHERE 
    LENGTH(content) > 15;
"""
