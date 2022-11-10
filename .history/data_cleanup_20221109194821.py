import pandas as pd
import datetime as dt
import uuid
import numpy as np


df = pd.read_csv('data/beiwe_test_data.csv')
df = pd.read_csv(df)

df.dtypes

##### CLEAN UP DATA FOR EVALUATION #####
countColumns = df.shape

sat_v_daysout = df['DaysOutGPS', 'home', 'Satisfaction']
