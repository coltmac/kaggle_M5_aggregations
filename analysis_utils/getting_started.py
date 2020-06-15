"""
Joins all the source data together into 'df'

Credit to https://www.kaggle.com/ryuheeeei/let-s-start-from-here-beginners-data-analysis
    who originally made this function.  (*: edits were made)
"""

import gc
import numpy as np
import pandas as pd
from analysis_utils.pull_data import pull_data

calendar_df, sales_train_validation_df, sample_submission_df, sell_prices_df = pull_data()

def make_dataframe():
    # Wide format dataset
    df_wide_train = sales_train_validation_df.drop(
        columns=["item_id", "dept_id", "cat_id", "state_id", "store_id", "id"]).T
    df_wide_train.index = calendar_df["date"][:1913]
    df_wide_train.columns = sales_train_validation_df["id"]

    # Making test label dataset
    df_wide_test = pd.DataFrame(np.zeros(shape=(56, len(df_wide_train.columns))), index=calendar_df.date[1913:],
                                columns=df_wide_train.columns)
    df_wide = pd.concat([df_wide_train, df_wide_test])

    # Convert wide format to long format
    df_long = df_wide.stack().reset_index(1)
    df_long.columns = ["id", "value"]

    del df_wide_train, df_wide_test, df_wide
    gc.collect()

    df = pd.merge(pd.merge(df_long.reset_index(), calendar_df, on="date"), sell_prices_df, on=["id", "wm_yr_wk"])
    df = df.drop(columns=["d"])
    df["sell_price"] = df["sell_price"].astype("float32")
    df["value"] = df["value"].astype("int32")
    df["state_id"] = df["store_id"].str[:2].astype("category")
    df = df.assign(revenue=df[['value', 'sell_price']].product(axis=1))

    del df_long
    gc.collect()

    return df

if __name__ == "__main__":
    df = make_dataframe()
    print(df.head(10))
    print(df.columns)