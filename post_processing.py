from __future__ import print_function

import os, sys
import pandas as pd
import scipy

sys.path.insert(0, 'post_processing')
from load_data import load_csv

# MY CSV
csv_name = '1_static_front_10m_ft'
my_csv_path = os.path.join('acquired_data', 'csv_data')

# MY AUDIOS


df_my_timestamps = load_csv(my_csv_path, csv_name)

scipy.io.wavfile.read()