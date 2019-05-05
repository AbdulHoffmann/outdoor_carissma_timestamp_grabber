import arrow
import time
import numpy as np
import pandas as pd

def capture_loop(duration, sp, data_container, time_compensation) -> np.array:
    for i in range(int(duration*1000/sp)):
        utc_timestamp = round(arrow.utcnow().float_timestamp, 3)
        utc_timestamp_millis = str(utc_timestamp).replace('.', '')
        data_container[i] = utc_timestamp_millis
        time.sleep(sp/1000 - time_compensation/1000)  # sampling rate control
    return data_container

def generate_timestamp(duration, sp, data_container, time_compensation):
    timestamp_array = capture_loop(
        duration, sp, 
        data_container, 
        time_compensation)
    timestamp_series = pd.Series(timestamp_array.astype(int)) 
    print(timestamp_series)
    
