# statistik.py
from pandas.core.indexes.base import Index
import streamlit as st
import datetime
import pandas as pd
import numpy as np
from backend.database import database
from backend.defines import DEFINES

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

    #for debug
    st.write(sd)
    st.write(ed)
    
    db = database()
    data = db.getAllData() #methode return a df 
    
    # Download button
    @st.cache
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    
    csv = convert_df(data)
    # Graph    
    df = pd.DataFrame(data,columns=['Zeit','Leistung']
    ).set_index(data['Zeit'])
    st.write(df)
    # st.bar_chart(df)


    service_list = DEFINES.getServiceList()#.append('Zeit')

    time = df['Zeit']

    service_df = pd.DataFrame(columns=service_list)
    service_df['Datum'] = time
    st.write(service_df)

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


    
