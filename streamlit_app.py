import streamlit

streamlit.title ('My parents New Healthy Diner')               
                 
streamlit.header ('Breakfast Menu')                 
streamlit.text ('🥣 Omega 3 & blueberry oatmeal')                 
streamlit.text   ('🥗 Kale, Spinach and Rocket Smoothie')                 
streamlit.text  ('🐔 Hard-Boiled free-range eggs')
streamlit.text  ('🥑🍞 Avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
