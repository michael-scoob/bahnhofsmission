# statistik.py
from json import encoder
from pandas.core.indexes.base import Index
import streamlit as st
import datetime
import pandas as pd
import numpy as np
import altair as alt
from backend.database import database
from backend.defines import DEFINES


# Download button
@st.cache
def convert_df(df):
# IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def app():
    st.title('Statistik')
    db = database()
    data = db.getAllData() #methode return a df 
    today = datetime.date.today()
    
  
    st.subheader("Alle Daten anschauen oder downloaden ")
    c1, c2 , c3 , c4 = st.columns((1, 1, 1, 1)) 
    
    if c1.button("Daten anzeigen",key="dw"):
        #db = database()
        db_data = db.getAllData()
        st.table(db_data)
    
    csv = convert_df(data)
    c2.download_button(
        label="CSV Download",
        data=csv,
        file_name=str(today) + '.csv',
        mime='text/csv',)

    if c4.button("Alle Daten löschen",key="adl"):
        db.clearAllData()
        db_data = db.getAllData()
        st.table(db_data)




    
