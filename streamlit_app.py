import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.title('My mom''s new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text(' 🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗 Kale ,spinach and rocket smoothie')
streamlit.text(' 🐔 Hard Boiled Free - Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')




fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return  fruityvice_normalized
  
def get_food_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("SELECT * from fruit_load_list")
          return my_cur.fetchall()
          
def add_fruit(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('"+new_fruit+"')")
          return 'Thanks for adding '+new_fruit
          
     



streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please enter the fruit name to get information")
  else:
    value_returned=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(value_returned)
except:
  streamlit.error()


streamlit.title('View our fruit list- Add your favourites')
if streamlit.button('Get the fruit list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     return_list=get_food_list()
     streamlit.header("The fruit load list contains")
     streamlit.dataframe(return_list)
     my_cnx.close()
    
  
#streamlit.stop()





second_choice = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     function_returned =add_fruit(second_choice)
     streamlit.text(function_returned)
     my_cnx.close()

