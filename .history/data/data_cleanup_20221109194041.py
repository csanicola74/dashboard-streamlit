import pandas as pd
import datetime as dt
import uuid
import numpy as np


df = ('data/beiwe_test_data.csv')

##### CLEAN UP DATA FOR EVALUATION #####
countColumns = df.shape

sat_v_daysout = df['DaysOutGPS', 'home', 'Satisfaction']
