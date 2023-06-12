import streamlit
import pandas
import requests
import snowflake.connector

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



streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json())

# normalizing the content 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# putting it in a table
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)

second_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding', second_choice)
mycur.exec("insert into food_load_list values ('from streamlit')");

