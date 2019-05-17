from __future__ import print_function

import os, sys
import pandas as pd
import librosa
import scipy.io
from collections import namedtuple

sys.path.insert(0, 'post_processing')
from load_data import load_csv, load_mat

# MY CSV
csv_name = '1_static_front_10m_ft'
my_csv_path = os.path.join('acquired_data', 'csv_data')
# MY AUDIOS
audio_names = ('FL', 'FR', 'BR', 'BL')
audio_path = os.path.join('acquired_data', 'raw_audios', '1')
# CARISSMA FILES
smart_path = os.path.join('acquired_data', 'mat_files', 'Smart')
Q7_path = os.path.join('acquired_data', 'mat_files', 'Smart')
mat_name = 'Siren_0001'

# Initializations
audios = dict()
sampling_rates = []

# Load data
df_my_timestamps = load_csv(my_csv_path, csv_name)
for audio_name in audio_names:
    audios[audio_name], sr = librosa.load(os.path.join(audio_path, audio_name + '.wav'), sr=None)
    sampling_rates.append(sr)
mic_mat, siren_mat = load_mat(
    mic_path=smart_path,
    siren_path=Q7_path,
    mat_name=mat_name
    )

# Operations
for name, audio in audios.items():
    print(name)
    print(audio.shape)

print(mic_mat['Data1_GPS_Time_msec___Time_in_M'].shape)
print(mic_mat['Data1_GPS_Time_Week___Start_0h_'].shape)
print(mic_mat['Data1_INS_Time_msec___Time_in_M'].shape)
print(mic_mat['Data1_INS_Time_Week___Weeks__St'].shape)

print(siren_mat['Data1_GPS_Time_msec___Time_in_M'].shape)
print(siren_mat['Data1_GPS_Time_Week___Start_0h_'].shape)
print(siren_mat['Data1_INS_Time_msec___Time_in_M'].shape)
print(siren_mat['Data1_INS_Time_Week___Weeks__St'].shape)

# TODO: Crop audio to match my_csv. 

SystemExit