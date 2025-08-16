import streamlit as st
import pandas as pd
import numpy as np
 
#---App Title AND Description ----
st.title('my first streamlit app')
st.write('this is a simple APP to demonsrate the basic fumctionalitis of streamlit.')

#----- Interactive widgets in the slidebar---
st.sidebar.header('user input features') 

# Text Input
user_name = st.sidebar.text_input('what is your name?','Savitri Reddy')

# slider
age = st.sidebar.slider('select your age', 0,100,25)

#Select box
favorite_color = st.sidebar.selectbox('what is fovorite color?',['Blue','Red','Green','Yellow'])

# --- main page content ---
st.header(f'welcome,{user_name}!')
st.write(f'you are {age} years old and your favorite color is {favorite_color}.')

#--- Displaying data---
st.subheader("Here's some random data:")

# Create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10,5),
    columns = ('col %d' % i for i in range(5))
)

st.dataframe(data)

#--- checkbox to show/hide content ---
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)
    
# --- Button to trigger action ---
if st.button('say hello'):
    st.write('hello there!')
else:
    st.write('good bye')        