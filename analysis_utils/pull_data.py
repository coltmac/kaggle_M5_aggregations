import pandas as pd
import os
from pathlib import Path

def pull_data():
    if Path(os.getcwd()).name == 'm5-forecasting-accuracy' or Path(os.getcwd()).name == 'kaggle_M5_aggregations':
        DATA_DIR = Path(os.getcwd())
    else:
        DATA_DIR = Path(os.getcwd()).parent

    calendar_df = pd.read_csv(DATA_DIR / 'data/calendar.csv')
    sales_train_validation_df = pd.read_csv(DATA_DIR / 'data/sales_train_validation.csv')
    sample_submission_df = pd.read_csv(DATA_DIR / 'data/sample_submission.csv')
    sell_prices_df = pd.read_csv(DATA_DIR / 'data/sell_prices.csv')

    sell_prices_df['id'] = sell_prices_df['item_id'] + '_' + sell_prices_df['store_id'] + '_validation'
    sell_prices_df = pd.concat([sell_prices_df, sell_prices_df["item_id"].str.split("_", expand=True)], axis=1)
    sell_prices_df = sell_prices_df.rename(columns={0: "cat_id", 1: "dept_id"})
    sell_prices_df[["store_id", "item_id", "cat_id", "dept_id"]] = sell_prices_df[["store_id", "item_id", "cat_id", "dept_id"]].astype("category")
    sell_prices_df = sell_prices_df.drop(columns=2)

    return calendar_df, sales_train_validation_df, sample_submission_df, sell_prices_df

if __name__ == "__main__":
    calendar_df, sales_train_validation_df, sample_submission_df, sell_prices_df = pull_data()
    print('calendar_df', '\n', calendar_df.head(), '\n', calendar_df.shape)
    print('sales_train_validation_df', '\n', sales_train_validation_df.head(), '\n', sales_train_validation_df.shape)
    print('sample_submission_df', '\n', sample_submission_df.head(), '\n', sample_submission_df.shape)
    print('sell_prices_df', '\n', sell_prices_df.head(), '\n', sell_prices_df.shape)