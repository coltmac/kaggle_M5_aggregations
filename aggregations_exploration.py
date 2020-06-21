import os
from pathlib import Path
import psutil
from analysis_utils.aggregation_levels import *
from analysis_utils.getting_started import make_dataframe
import time

start_time = time.time()

process = psutil.Process(os.getpid())
print('start memory size (Mb): ', process.memory_info().rss / 1_000_000)

df = make_dataframe()

process = psutil.Process(os.getpid())
print('make_dataframe done (Mb): ', process.memory_info().rss / 1_000_000)

agg_12 = make_agg_12(df)
agg_11 = make_agg_11(agg_12)
agg_10 = make_agg_10(agg_11)

agg_list = [agg_12, agg_11, agg_10]
agg_str = ['agg_12', 'agg_11', 'agg_10']
cwd = Path(os.getcwd())
target = 'data/aggregations/'
for agg_i, agg in enumerate(agg_list):
    agg_name = agg_str[agg_i]
    agg.to_csv(cwd / target / f'{agg_name}.csv', index=False)
    print('wrote: ', f'{agg_name}.csv')

agg_9 = make_agg_9(agg_12)
agg_8 = make_agg_8(agg_9)
agg_7 = make_agg_7(agg_9)
agg_6 = make_agg_6(agg_7)
agg_5 = make_agg_5(agg_7)
agg_4 = make_agg_4(agg_8)
agg_3 = make_agg_3(agg_8)
agg_2 = make_agg_2(agg_6)
agg_1 = make_agg_1(agg_2)

print('aggregations 1-12 made. Memory: ', process.memory_info().rss / 1_000_000)


""" as a convenience, this step saves the aggregations locally so this doesn't need to run again. """
cwd = Path(os.getcwd())
target = 'data/aggregations/'

# template: agg_12.to_csv(cwd / target / 'agg_12.csv', index=False)
agg_list = [agg_9, agg_8, agg_7, agg_6, agg_5, agg_4, agg_3, agg_2, agg_1]
agg_str = ['agg_9', 'agg_8', 'agg_7', 'agg_6', 'agg_5', 'agg_4', 'agg_3', 'agg_2', 'agg_1']

for agg_i, agg in enumerate(agg_list):
    agg_name = agg_str[agg_i]
    agg.to_csv(cwd / target / f'{agg_name}.csv', index=False)
    print('wrote: ', f'{agg_name}.csv')


print("--- %s seconds ---" % (time.time() - start_time))
print('done')
