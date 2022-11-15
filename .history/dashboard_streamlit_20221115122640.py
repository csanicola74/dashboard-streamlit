#### Imports ####

import pandas as pd
import streamlit as st

#### First Dataframe - Head 100 ####

df = pd.read_csv('DOHMH_Dog_Bite_Data.csv')

df = df.head(100)

#### Header ####

st.header('Dog Bite Incidents: 2015 to 2017')

#### Caption ####

st.caption('The Statewide Planning and Research Cooperative System (SPARCS) Inpatient De-identified File contains discharge level detail on patient characteristics, diagnoses, treatments, services, and charges. This data file contains basic record level detail for the discharge. The de-identified data file does not contain data that is protected health information (PHI) under HIPAA. The health information is not individually identifiable; all data elements considered identifiable have been redacted. For example, the direct identifiers regarding a date have the day and month portion of the date removed.')

#### Toggle ####

if st.checkbox('Show first 100 records of DOHMH Dog Bite Dataset'):
    st.dataframe(df)

#### Code Block ####

code = '''## Wondering how we included the toggle feature?
if st.checkbox('Show first 100 records of DOHMH Dog Bite Dataset'):
    st.dataframe(df)'''
st.code(code, language='python')

#### Second Dataframe ####

st.subheader('Breed Count')

df = pd.read_csv('DOHMH_Dog_Bite_Data.csv')

breed_count = df['Breed'].value_counts()

breed_count

st.caption("Here is the data summarized by breed")

#### Barchart - Bite Incidents by Breed ####

st.subheader('Bite Incidents by Breed')

st.area_chart(breed_count)

st.caption("Here is a simple bar graph representation of bite incident by breed according to the dataset")


#### Line Chart - Bite Incidents over time ####

st.subheader('Bite Incidents From 2015 to 2017')

over_time = df['DateOfBite'].value_counts()

st.line_chart(over_time)

st.caption("Here is a line chart displaying bite incidents over time")
