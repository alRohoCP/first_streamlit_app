# Libraries
import streamlit
import pandas
import requests

# Imported files
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# We want to see the number of the fruits as id_row or index, not a numerical ID
my_fruit_list = my_fruit_list.set_index('Fruit')

# Fruitvyce api respones
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Streamlit Code
streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#Interaction with the table to pick the fruits customers want to include. We have selected by default Avocado and Strawberries
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# With this code we filter the table with the selected fruits (at first instance, the selected fruits by default)
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Smoothies table 
streamlit.dataframe(fruits_to_show)

#API response
streamlit.text(fruityvice_response)

