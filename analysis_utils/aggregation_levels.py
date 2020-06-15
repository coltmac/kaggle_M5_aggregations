"""
create functions to create each of the 12 aggregation levels described in Kaggle's M5-Competitors-Guide-Final-10-March-2020 word doc.
"""
import pandas as pd


def make_agg_12(input_df):
    """
    :param input_df: This should be the 'df' created by getting_started.py
    :return: agg_12: Unit sales of product x, aggregated for each store
    """
    for header in list(input_df):
        if (str(input_df[header].dtypes) != 'category') & (not pd.api.types.is_numeric_dtype(input_df[header].dtypes)):
            input_df.loc[input_df[header].isna(), header] = 'none'
    print('agg_12 made')
    return input_df


def make_agg_11(input_df):
    """
    :param input_df: agg_12
    :return: agg_11: Unit sales of product x, aggregated for each State
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI',
                      'item_id', 'state_id', 'cat_id', 'dept_id',
                      'value', 'sell_price', 'revenue']] # removed ['id','store_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'item_id', 'cat_id', 'dept_id',
                         'state_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_11 made')
    return out


def make_agg_10(input_df):
    """
    :param input_df: agg_11
    :return: agg_10: Unit sales of product x, aggregated for all stores/states
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI',
                      'item_id', 'cat_id', 'dept_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','state_id','store_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'item_id', 'cat_id', 'dept_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_10 made')
    return out


def make_agg_9(input_df):
    """
    :param input_df: agg_12
    :return: agg_9: Unit sales of all products, aggregated for each store and department
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI',
                      'state_id', 'store_id', 'cat_id', 'dept_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','item_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'state_id','store_id', 'cat_id', 'dept_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_9 made')
    return out


def make_agg_8(input_df):
    """
    :param input_df: agg_9
    :return: agg_9: Unit sales of all products, aggregated for each store and category
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI',
                      'state_id', 'store_id', 'cat_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','item_id','dept_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'store_id', 'cat_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_8 made')
    return out


def make_agg_7(input_df):
    """
    :param input_df: agg_9
    :return: agg_8: Unit sales of all products, aggregated for each State and department
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'cat_id', 'dept_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','store_id','item_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'cat_id', 'dept_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_7 made')
    return out


def make_agg_6(input_df):
    """
    :param input_df: agg_7
    :return: agg_6: Unit sales of all products, aggregated for each State and category
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'cat_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','store_id','item_id','dept_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'cat_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_6 made')
    return out


def make_agg_5(input_df):
    """
    :param input_df: agg_7
    :return: agg_5: Unit sales of all products, aggregated for each department
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI', 'cat_id', 'dept_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','store_id','item_id','state_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'cat_id', 'dept_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_5 made')
    return out


def make_agg_4(input_df):
    """
    :param input_df: agg_8
    :return: agg_4: Unit sales of all products, aggregated for each category
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI', 'cat_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','store_id','item_id','state_id','dept_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'cat_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_4 made')
    return out


def make_agg_3(input_df):
    """
    :param input_df: agg_8
    :return: agg_3: Unit sales of all products, aggregated for each store
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'store_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','cat_id', 'dept_id', 'item_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'state_id', 'store_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_3 made')
    return out


def make_agg_2(input_df):
    """
    :param input_df: agg_6
    :return: agg_2: Unit sales of all products, aggregated for each State
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI', 'state_id',
                      'value', 'sell_price', 'revenue']]  # removed ['id','cat_id','dept_id','item_id','store_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI', 'state_id'], observed=True).sum()
    out = out.reset_index()
    print('agg_2 made')
    return out


def make_agg_1(input_df):
    """
    :param input_df: agg_2
    :return: agg_1: Unit sales of all products, aggregated for all stores/states
    """
    clean = input_df[['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                      'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                      'snap_CA', 'snap_TX', 'snap_WI',
                      'value', 'sell_price', 'revenue']]  # removed ['id','cat_id','dept_id','item_id','store_id','state_id']
    out = clean.groupby(['date', 'wm_yr_wk', 'weekday', 'wday', 'month', 'year',
                         'event_name_1', 'event_type_1', 'event_name_2', 'event_type_2',
                         'snap_CA', 'snap_TX', 'snap_WI'], observed=True).sum()
    out = out.reset_index()
    print('agg_1 made')
    return out


if __name__ == "__main__":
    from getting_started import make_dataframe
    from analysis_utils.pull_data import pull_data

    calendar_df, sales_train_validation_df, sample_submission_df, sell_prices_df = pull_data()

    df = make_dataframe()

    agg_12 = make_agg_12(df)
    agg_11 = make_agg_11(agg_12)
    agg_10 = make_agg_10(agg_11)
    agg_9 = make_agg_9(agg_12)
    agg_8 = make_agg_8(agg_9)
    agg_7 = make_agg_7(agg_9)
    agg_6 = make_agg_6(agg_7)
    agg_5 = make_agg_5(agg_7)
    agg_4 = make_agg_4(agg_8)
    agg_3 = make_agg_3(agg_8)
    agg_2 = make_agg_2(agg_6)
    agg_1 = make_agg_1(agg_2)

