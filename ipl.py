import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open(r'pipe.pkl','rb'))


teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Delhi Capitals',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab']

cities=['Mumbai',
 'Kolkata',
 'Bangalore',
 'Chennai',
 'Chandigarh',
 'Jaipur',
 'Hyderabad',
 'Dubai',
 'Abu Dhabi',
 'Sharjah',
 'Bengaluru',
 'Durban',
 'Delhi',
 'Ahmedabad',
 'Pune']


st.title('Ipl Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


