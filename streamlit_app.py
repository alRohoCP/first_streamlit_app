# Libraries
import streamlit
import pandas

# Imported files
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# We want to see the number of the fruits as id_row or index, not a numerical ID
my_fruit_list = my_fruit_list.set_index('Fruit')

# Streamlit Code
streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#Interaction with the table to pick the fruits customers want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Smoothies table 
streamlit.dataframe(my_fruit_list)


