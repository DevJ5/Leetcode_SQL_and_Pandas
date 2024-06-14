import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(visits, transactions, on="visit_id", how="left")
    df = df[df["transaction_id"].isnull()]
    df = df.groupby("customer_id").size().reset_index(name="count_no_trans")
    return df


# select customer_id, count(*) as count_no_trans
# from Visits as V
# left join Transactions as T on V.visit_id = T.visit_id
# where T.transaction_id is null
# group by customer_id
