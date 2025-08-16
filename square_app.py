# 1. import streamlit
import streamlit as st

# 2. # add title to your APP
st.title('this is my frst streamlit APP created by SAVITRI REDDY')   

# 3. # add some TEXT
st.write('welcome ! this APP calculates the suare of a number.') 

#4. create a interactive slider
st.header('select a number')
number = st.slider('pick a number',0,100,25)   # min ,max,default

#5. calculate and display the result
st.subheader('result')
squared_number = number * number
st.write(f'the square of **{number}** is **{squared_number}**,')
