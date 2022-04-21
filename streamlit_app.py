# Libraries
import streamlit
import pandas
import requests
import snowflake.connector

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


#Interaction with the table to pick the fruits customers want to include. We have selected by default Avocado and Strawberries
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# With this code we filter the table with the selected fruits (at first instance, the selected fruits by default)
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Smoothies table 
streamlit.dataframe(fruits_to_show)

#API response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

#Adding snowflake queried info
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)



# Fruitvyce api respones
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# This just writes the data to the screen 
# streamlit.text(fruityvice_response.json())
# let's normalize the text using a dataframe

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

