import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    subset = tweets[tweets["content"].str.len() > 15]
    return subset[["tweet_id"]]


# select tweet_id
# from Tweets
# where LENGTH(content) > 15
