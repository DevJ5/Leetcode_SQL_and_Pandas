import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    subset = views[views["author_id"] == views["viewer_id"]]
    subset = sorted(subset["author_id"].unique())

    return pd.DataFrame({"id": subset})


# select distinct author_id as id
# from Views
# where author_id = viewer_id
# order by id asc
