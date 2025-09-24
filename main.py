#Run imports
import streamlit as st
import pandas as pd

#Create the table with the appropiate columns and rows 
data={'Material name':['Leather','Iron', 'Animal bone', 'Ebony'],'Normal':[0,0,0,0], 'Advanced':[0,0,0,0],'Elite':[0,0,0,0],'Epic':[0,0,0,0],'Legendary':[0,0,0,0] }
#Pass it to a pandas dataframe
df= pd.DataFrame(data)
#Convert it into a st.data_editor
st.write("#Material table")
table= st.data_editor(df, num_rows= 'dynamic', key= 'table')