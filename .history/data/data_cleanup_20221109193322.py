import numpy as np
import pandas as pd

df = ('data/dmps4192_merged_with_questions.csv')

##### CLEAN UP DATA FOR EVALUATION #####
countRows, countColumns = df.shape

sat_v_daysout = df['DaysOutGPS', 'home', 'Satisfaction']
