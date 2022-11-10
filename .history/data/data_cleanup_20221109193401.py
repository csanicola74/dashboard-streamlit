import pandas as pd
import datetime as dt
import uuid
import numpy as np


df = ('data/dmps4192_merged_with_questions.csv')

##### CLEAN UP DATA FOR EVALUATION #####
countColumns = df.shape

sat_v_daysout = df['DaysOutGPS', 'home', 'Satisfaction']
