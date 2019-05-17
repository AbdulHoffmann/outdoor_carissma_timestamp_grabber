from __future__ import print_function

import pandas as pd
import os

def load_csv(csv_path, csv_name):
    df_my_recordings = pd.read_csv(os.path.join(csv_path, csv_name + '.csv'), names=['index', 'timestamp'])
    df_my_recordings.set_index('index', inplace=True)
    df_my_recordings['timestamp'] = df_my_recordings['timestamp'].apply(
        lambda x: x if len(str(x)) == 13 else int(str(x) + '0')
        )  # add a single zero so data has the same length
    df_my_recordings['difference'] = df_my_recordings.diff(axis=0)

    print(df_my_recordings, end='\n\n')

    print('sampling mean:', round(df_my_recordings['difference'].mean(), 3))
    print('sampling median: ', df_my_recordings['difference'].median())
    return df_my_recordings
    