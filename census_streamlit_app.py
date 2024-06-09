import streamlit as st

from pymongo.mongo_client import MongoClient
client=MongoClient("mongodb+srv://riyazudeen74:1234@cluster0.9lpp0xg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test.riyaz


st.title("What is the total population of each district?")

st.write(f"{item['name']} has a :{item['pet']}:")

