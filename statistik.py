# statistik.py
from pandas.core.indexes.base import Index
import streamlit as st
import datetime
import pandas as pd
import numpy as np
from backend.database import database

def app():
    st.title('Statistik')
    st.write('Auswertung der Daten über auszuwählende Zeiträume. Bitte einen Zeitraum wählen!')
    year=str(datetime.date.year)
    month=str(datetime.date.month)
    day=str(datetime.date.day)
    today = datetime.date.today()
    
    # Datum auswahl
    sd = st.date_input("Start Datum wählen", today,max_value=today,key="sd")
    ed = st.date_input("End Datum wählen", today,max_value=today,key="ed")

    db = database()
    data = db.getAllData() #methode return a df 
    
    # Download button
    @st.cache
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    
    csv = convert_df(data)

    # Graph
    st.title('Leistungen')
    
    
    df = pd.DataFrame(data,columns=['Leistung'])
    #df.set_index(['Zeit'])
    st.bar_chart(df)
    
    tdf = pd.DataFrame(data,columns=['Leistung']
    ).set_index(data['Zeit'])
    
    st.write(tdf)
    st.bar_chart(tdf)
    
    # tdata = pd.DataFrame({
    # 'index': ['Cincinnati', 'San Francisco', 'Pittsburgh'],
    # 'sports_teams': [6, 8, 9],
    # }).set_index('index')
    # st.write(tdata)
    # st.bar_chart(tdata)

    st.download_button(
        label="Download",
        data=csv,
        file_name=str(today) + '.csv',
        mime='text/csv',
    )
    

    
    #  
    if st.button("Daten anschauen!",key="dw"):
        db = database()
        db_data = db.getAllData()
        st.table(db_data)


    
