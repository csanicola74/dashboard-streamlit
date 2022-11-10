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
    return data_1


data_1_load_state = st.text('Loading data...')
data_1 = load_data(10000)
data_1_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data for Dataframe 1 [Subject1]', key='1'):
    st.subheader('Raw data')
    st.write(data_1)


@st.cache
def load_data(nrows):
    data_2 = pd.read_csv(DATA_URL_2, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data_2.rename(lowercase, axis='columns', inplace=True)
    data_2[DATE_COLUMN_2] = pd.to_datetime(data_2[DATE_COLUMN_2])
    return data_2


data_2_load_state = st.text('Loading data...')
data_2 = load_data(10000)
data_2_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data for Dataframe 2 [Subject2]', key='2'):
    st.subheader('Raw data')
    st.write(data_2)


df_1 = pd.read_csv('data/dmps4192 mergedSummaryExerciseData.csv')

st.subheader('Satisfaction vs. Ability for Subject 1')
sat_v_abil = df_1[['Ability', 'Satisfaction']]
st.line_chart(sat_v_abil)

df_2 = pd.read_csv('data/5glhn8oo mergedSummaryExerciseData.csv')

st.subheader('Satisfaction vs. Ability for Subject 2')
sat_v_abil = df_2[['Ability', 'Satisfaction']]
st.line_chart(sat_v_abil)
