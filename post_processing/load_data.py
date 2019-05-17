from __future__ import print_function

import pandas as pd
import numpy as np
import os
import scipy.io
import pandas as pd

def load_csv(csv_path, csv_name):
    df_my_recordings = pd.read_csv(os.path.join(csv_path, csv_name + '.csv'), names=['index', 'timestamp'])
    df_my_recordings.set_index('index', inplace=True)
    df_my_recordings['timestamp'] = df_my_recordings['timestamp'].apply(
        lambda x: x if len(str(x)) == 13 else int(str(x) + '0')
        )  # add a single zero so data has the same length
    df_my_recordings['difference'] = df_my_recordings.diff(axis=0)

    # print(df_my_recordings, end='\n\n')

    print('sampling mean:', round(df_my_recordings['difference'].mean(), 3))
    print('sampling median: ', df_my_recordings['difference'].median())
    return df_my_recordings

def load_mat(mic_path, siren_path, mat_name):
    mat_mic = scipy.io.loadmat(os.path.join(mic_path, mat_name + '.mat'))
    mat_siren = scipy.io.loadmat(os.path.join(mic_path, mat_name + '.mat'))

    mat_mic = np.array(
        [mat_mic['Data1_GPS_Time_msec___Time_in_M'],
        mat_mic['Data1_GPS_Time_Week___Start_0h_'],
        mat_mic['Data1_INS_Time_msec___Time_in_M'],
        mat_mic['Data1_INS_Time_Week___Weeks__St']],
        dtype={
            'names':(
                'Data1_GPS_Time_msec___Time_in_M', 
                'Data1_GPS_Time_Week___Start_0h_', 
                'Data1_INS_Time_msec___Time_in_M', 
                'Data1_INS_Time_Week___Weeks__St'
            ),
            'formats':(
                np.float, np.float, np.float, np.float
            )
        }
    )

    mat_siren = np.array(
        [mat_siren['Data1_GPS_Time_msec___Time_in_M'],
        mat_siren['Data1_GPS_Time_Week___Start_0h_'],
        mat_siren['Data1_INS_Time_msec___Time_in_M'],
        mat_siren['Data1_INS_Time_Week___Weeks__St']],
        dtype={
            'names':(
                'Data1_GPS_Time_msec___Time_in_M', 
                'Data1_GPS_Time_Week___Start_0h_', 
                'Data1_INS_Time_msec___Time_in_M', 
                'Data1_INS_Time_Week___Weeks__St'
            ),
            'formats':(
                np.float, np.float, np.float, np.float
            )
        }
    )

    return mat_mic, mat_siren
