import streamlit as st
import pandas as pd
import numpy as np

st.title('Beiwe Data Dashboard')

DATE_COLUMN = 'time_locs'
DATA_URL = ('data/dmps4192 mergedSummaryExerciseData.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

df = pd.read_csv('data/dmps4192 mergedSummaryExerciseData.csv')

st.subheader('Satisfaction vs. Days Out and Days In')
sat_v_daysout = df[['DaysOutGPS', 'home', 'Satisfaction']]
st.bar_chart(sat_v_daysout)

st.subheader('Satisfaction vs. Ability')
sat_v_abil = df[['Ability', 'Satisfaction']]
st.line_chart(sat_v_abil)
