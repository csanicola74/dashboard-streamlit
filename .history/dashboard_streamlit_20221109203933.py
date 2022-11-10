import streamlit as st
import pandas as pd
import numpy as np

st.title('Beiwe Data Dashboard')

DATE_COLUMN_1 = 'time_locs'
DATA_URL_1 = ('data/dmps4192 mergedSummaryExerciseData.csv')

DATE_COLUMN_2 = 'time_locs'
DATA_URL_2 = ('data/5glhn8oo mergedSummaryExerciseData.csv')


@st.cache
def load_data(nrows):
    data_1 = pd.read_csv(DATA_URL_1, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data_1.rename(lowercase, axis='columns', inplace=True)
    data_1[DATE_COLUMN_1] = pd.to_datetime(data_1[DATE_COLUMN_1])
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL_2, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN_2] = pd.to_datetime(data[DATE_COLUMN_2])
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


df = pd.read_csv('data/dmps4192 mergedSummaryExerciseData.csv')

st.subheader('Satisfaction vs. Ability')
sat_v_abil = df[['Ability', 'Satisfaction']]
st.line_chart(sat_v_abil)
