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
    st.subheader("Leitungen im Zeitraum suchen ...")
    c1, c2 = st.columns((1, 1)) 
    sd = c1.date_input("Von ", today,max_value=today,key="sd")
    ed = c2.date_input("Bis", today,max_value=today,key="ed")

    if ed < sd:
        st.info('Bitte Zeitraum prüfen!')
    
    db = database()
    data = db.getAllData() #methode return a df 
    
    # Download button
    @st.cache
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    csv = convert_df(data)

    # Create df with time and service from db data
    db_df = pd.DataFrame(data,columns=['Zeit','Leistung'])
    # st.subheader("Database")
    # st.write(db_df)
    

    # Get the define of services and create service df
    service_list = DEFINES.getServiceList()
    time = db_df['Zeit']
    _df = pd.DataFrame(columns=service_list)
    _df.insert(loc=0,column='Zeit',value=time)
    service_df = pd.DataFrame(_df)#.set_index(_df['Datum'])
    st.subheader("Leistungen")
    #st.write(service_df)

    # put and separete values of service into service df

    for index , row in db_df.iterrows():
        #st.write("DB Text in dem gesucht wird ..: \n" + str(db_df))
        #st.write("Index: " + str(index))
        value = str(db_df['Leistung'].iloc[index])
        service_db_value_list =  value.split(';')

        #ToDo - Listen vergleichen
        for i in service_db_value_list:
            #i=index
            for j in service_list:
                if(i ==j):
                    #st.info("Gefunden: " + i)
                    service_df[i][index] =  str('X')
                    #st.write(service_df)
                    break
                    

    #st.write(service_df)

        #ToDo - Werte in service_df ablegen

    #st.write(service_db_value_list)

    # Get slice of dataframe by date
    service_time_df=service_df.set_index('Zeit')
    #st.write(service_time_df)
    timeslice =service_time_df.loc[str(sd):str(ed)]
    #timeslice =service_time_df.loc[str(datetime.date.today):str(datetime.date.today)]
    #st.write('Zeitraum von ' + str(sd) + " bis " + str(ed) )
    st.write(timeslice)

    st.subheader("Alle Daten downloaden ")
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


    
