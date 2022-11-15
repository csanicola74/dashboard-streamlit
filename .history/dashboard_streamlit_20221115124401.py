#### Imports ####

import pandas as pd
import streamlit as st

#### Pull in both Dataframe - Head 100 ####

df1 = pd.read_csv('5glhn8oo_clean_data.csv')
df2 = pd.read_csv('dmps4192_clean_data.csv')

#### Header ####

st.header('Beiwe Data Dashboard')

#### Caption ####

st.caption(
    'Data from the Beiwe dataset from Hannah Mercier and the Stony Brook OT Team.')

#### Toggle ####

if st.checkbox('Show Subject 1 Dataset'):
    st.dataframe(df1)

if st.checkbox('Show Subject 2 Dataset'):
    st.dataframe(df2)


#### Barchart - Depression ####

st.subheader('Reported Depressed State for Subject 1')
depressed = df1['Depressed'].value_counts()
st.bar_chart(depressed)
st.caption(
    "Here is a simple bar graph representation of the subjects reported level of depression.")


#### Line Chart - Bite Incidents over time ####

st.subheader('Type of Exercise for Subject 2')
exercise = df2[['HeavyEx', 'ModerateEx', 'LightEx', 'week']]
st.line_chart(exercise, x='week')
st.caption(
    "Here is a line chart displaying the type of exercise the subject reported doing each week")


#### Code Block ####

code = '''## Code behind the Line Chart for Subject 2
exercise = df2[['HeavyEx', 'ModerateEx', 'LightEx', 'week']]
st.line_chart(exercise, x='week')'''
st.code(code, language='python')
