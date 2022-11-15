import streamlit as st
import pandas as pd
import numpy as np

st.title('Beiwe Data Dashboard')
st.text('This is a dashboard for Beiwe data as analyzed by Caroline Sanicola.')

DATE_COLUMN_1 = 'time_locs'
DATA_URL_1 = (
    'https://github.com/csanicola74/dashboard-streamlit/blob/main/data/dmps4192_mergedSummaryExerciseData.csv')

DATE_COLUMN_2 = 'time_locs'
DATA_URL_2 = (
    'https://github.com/csanicola74/dashboard-streamlit/blob/main/data/5glhn8oo_mergedSummaryExerciseData.csv')


@st.cache
def load_data(nrows):
    data_1 = pd.read_csv(DATA_URL_1, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data_1.rename(lowercase, axis='columns', inplace=True)
    data_1[DATE_COLUMN_1] = pd.to_datetime(data_1[DATE_COLUMN_1])
    return data_1


@st.cache
def load_data(nrows):
    data_2 = pd.read_csv(DATA_URL_2, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data_2.rename(lowercase, axis='columns', inplace=True)
    data_2[DATE_COLUMN_2] = pd.to_datetime(data_2[DATE_COLUMN_2])
    return data_2


df_1 = pd.read_csv('data/dmps4192 mergedSummaryExerciseData.csv')

st.subheader('Satisfaction vs. Ability for Subject 1')
sat_v_abil = df_1[['Ability', 'Satisfaction']]
st.bar_chart(sat_v_abil, x='Ability', y='Satisfaction')

df_2 = pd.read_csv('data/5glhn8oo mergedSummaryExerciseData.csv')

st.subheader('Type of Exercise for Subject 2')
exercise = df_2[['HeavyEx', 'ModerateEx', 'LightEx', 'week']]
st.line_chart(exercise, x='week')

st.subheader('Code for Bar Chart')
code_1 = """st.subheader('Satisfaction vs. Ability for Subject 1')
sat_v_abil = df_1[['Ability', 'Satisfaction']]
st.bar_chart(sat_v_abil, x='Ability', y='Satisfaction')"""
st.code(code_1, language='python')

st.subheader('Code for Line Chart')
code_2 = """st.subheader('Type of Exercise for Subject 2')
    exercise = df_2[['HeavyEx', 'ModerateEx', 'LightEx', 'week']]
    st.line_chart(exercise, x='week')"""
st.code(code_2, language='python')
