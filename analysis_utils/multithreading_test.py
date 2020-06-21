"""
create functions to create each of the 12 aggregation levels described in Kaggle's M5-Competitors-Guide-Final-10-March-2020 word doc.
"""
import pandas as pd
import itertools
import multiprocessing as mp
from pathlib import Path
import os

cwd = Path(os.getcwd())
target = 'data/aggregations/'
#agg_12 = pd.read_csv(cwd / target / 'agg_12.csv')


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

data_iterator = pd.read_csv(cwd / target / 'agg_12.csv', chunksize=5_000_000)

chunk_list = []  

# Each chunk is in dataframe format
for data_chunk in data_iterator:  
    filtered_chunk = make_agg_9(data_chunk)
    chunk_list.append(filtered_chunk)
    
filtered_data = pd.concat(chunk_list)

agg_9 = make_agg_9(filtered_data)



if __name__ == "__main__":
    from getting_started import make_dataframe
    from analysis_utils.pull_data import pull_data

    calendar_df, sales_train_validation_df, sample_submission_df, sell_prices_df = pull_data()

    df = make_dataframe()

    """start"""





def stream_groupby_csv(path, key, input_agg, chunk_size=1e6, pool=None, **kwargs):

    # Make sure path is a list
    if not isinstance(path, list):
        path = [path]

    # Chain the chunks
    kwargs['chunksize'] = chunk_size
    chunks = itertools.chain(*[pd.read_csv(p, **kwargs) for p in path ])

    results = []
    orphans = pd.DataFrame()

    for chunk in chunks:

        # Add the previous orphans to the chunk
        chunk = pd.concat((orphans, chunk))

        # Determine which rows are orphans
        last_val = chunk[key].iloc[-1]
        is_orphan = chunk[key] == last_val

        # Put the new orphans aside
        chunk, orphans = chunk[~is_orphan], chunk[is_orphan]

        # If a pool is provided then we use apply_async
        if pool:
            results.append(pool.apply_async(input_agg, args=(chunk,)))
        else:
            results.append(input_agg(chunk))

    # If a pool is used then we have to wait for the results
    if pool:
        results = [r.get() for r in results]

    return pd.concat(results)

def input_agg(chunk):
    "lambdas can't be serialized so we need to use a function"
    return chunk.groupby('some_sub_key')['some_column'].sum()

cwd = Path(os.getcwd())
target = 'data/aggregations/'
agg_name = 'agg_12'
agg_12_path = cwd / target / f'{agg_name}.csv'

results = results = stream_groupby_csv(
    path=[
        agg_12_path
    ],
    key='date',
    agg=input_agg,
    chunk_size=200,
    pool=mp.Pool(processes=2)
)