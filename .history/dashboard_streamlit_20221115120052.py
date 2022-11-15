import streamlit as st
import pandas as pd
import numpy as np

st.title('Beiwe Data Dashboard')
st.text('This is a dashboard for Beiwe data as analyzed by Caroline Sanicola.')


df_1 = pd.read_csv(
    'https://github.com/csanicola74/dashboard-streamlit/blob/main/data/dmps4192_mergedSummaryExerciseData.csv')

st.subheader('Satisfaction vs. Ability for Subject 1')
sat_v_abil = df_1[['Ability', 'Satisfaction']]
st.bar_chart(sat_v_abil, x='Ability', y='Satisfaction')

df_2 = pd.read_csv(
    'dhttps://github.com/csanicola74/dashboard-streamlit/blob/main/data/5glhn8oo_mergedSummaryExerciseData.csv')

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
