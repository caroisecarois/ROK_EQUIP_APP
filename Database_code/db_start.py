import database as db
import streamlit as st
from sqlalchemy import create_engine

#Set up the db url using streamlit secrets 
db_url= st.secrets['connection']['db']['url']
#Create the sql engine and connection 
engine= create_engine(db_url)
conn= engine.connect()
#Set up the database with the new connection
try:
    db.start_database(conn)
except Exception as e:
    print(str(e))