import numpy as np
import pandas as pd

df = ('data/dmps4192_merged_with_questions.csv')

##### CLEAN UP DATA FOR EVALUATION #####
df.columns


sat_v_daysout = df['DaysOutGPS', 'home', 'Satisfaction']
st.line_chart(sat_v_daysout)
