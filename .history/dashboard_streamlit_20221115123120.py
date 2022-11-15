#### Imports ####

import pandas as pd
import streamlit as st

#### Pull in both Dataframe - Head 100 ####

df1 = pd.read_csv('data/5glhn8oo_clean_data.csv')
df2 = pd.read_csv('data/dmps4192_clean_data.csv')

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


#### Barchart - Satisfaction vs Ability ####

st.subheader('Satisfaction vs Ability')
st.bar_chart(df1[['Satisfaction', 'Ability']])
st.caption("Here is a simple bar graph representation of the subjects reported Satisfaction vs their reported Physical Ability")


#### Line Chart - Bite Incidents over time ####

st.subheader('Bite Incidents From 2015 to 2017')

over_time = df['DateOfBite'].value_counts()

st.line_chart(over_time)

st.caption("Here is a line chart displaying bite incidents over time")

#### Code Block ####

code = '''## Wondering how we included the toggle feature?
if st.checkbox('Show first 100 records of DOHMH Dog Bite Dataset'):
    st.dataframe(df)'''
st.code(code, language='python')
