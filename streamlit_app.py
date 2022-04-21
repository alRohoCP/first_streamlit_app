# Libraries
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#API response
streamlit.header('Fruityvice Fruit Advice!')
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

## Priori options, without selector error option    
# fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
# streamlit.write('The user entered', fruit_choice)
# Fruitvyce api respones
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# This just writes the data to the screen 
# streamlit.text(fruityvice_response.json())
# let's normalize the text using a dataframe
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# streamlit.dataframe(fruityvice_normalized)

streamlit.header("View Our Fruit List - Add your Favorites")
# Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
  
# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
  snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values (' " + new_fruit +" ')")
    return 'Thanks for adding' + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_fucntion = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.dataframe(back_from_function)


