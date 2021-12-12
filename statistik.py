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

# WORK
WORK = False


def app():
    st.title('Statistik')
    st.write('Auswertung der Daten über auszuwählende Zeiträume. Bitte einen Zeitraum wählen!')
    year=str(datetime.date.year)
    month=str(datetime.date.month)
    day=str(datetime.date.day)
    today = datetime.date.today()
    
    # Datum auswahl
    st.subheader("Bitte einen Zeitraum auswählen ...")
    c1, c2 = st.columns((1, 1)) 
    sd = c1.date_input("Von ", today,max_value=today,key="sd")
    ed = c2.date_input("Bis", today,max_value=today,key="ed")

    if ed < sd:
        st.info('Bitte Zeitraum prüfen!')
    else:
        db = database()
        data = db.getAllData() #methode return a df 
        #--------------------------------------------------------------
        # Personen Statistik
        st.markdown('----')
        #st.subheader('Personen Statistik')
        st.title("Besucher gesamt" )

        people_df = pd.DataFrame(data,columns=['Zeit','Geschlecht','Alter'])
        #people_df = people_df.set_index('Zeit')
        #st.write(people_df)
        
        mann = 0
        frau = 0
        divers = 0


        for index, row in people_df.iterrows():
            s = str(people_df['Geschlecht'].iloc[index])
            if s == ';':
                people_df['Geschlecht'].iloc[index] = str(0)
            elif s == 'Divers':
                divers = divers + 1
            elif s == 'Mann':
                mann = mann + 1
            elif s == 'Frau':
                frau = frau + 1
        st.write("Männer: " + str(mann) + " | Frauen: " + str(frau) + " | Divers: " + str(divers))

        unter_18 = 0
        bis_27 = 0
        bis_65 = 0
        über_65 = 0

        for index, row in people_df.iterrows():
            s = str(people_df['Alter'].iloc[index])
            if s == 'unter 18':
                unter_18 = unter_18 + 1
            elif s == 'bis 27 (inkl.)':
                bis_27 = bis_27 + 1
            elif s == 'bis 65 (inkl.)':
                bis_65 = bis_65 + 1
            elif s == 'über 65':
                über_65 = über_65 + 1
            else: 
                people_df['Alter'].iloc[index] = str('0')
            

        st.write("unter 18: " + str(unter_18) + " | bis 27: " + str(bis_27) + " |  bis 65: " + str(bis_65) + " | über 65: " + str(über_65))

        if WORK:
            people_time_df=people_df.set_index('Zeit')
            timeslice_df =people_time_df.loc[str(sd):str(ed)]
            timeslice_df = timeslice_df.sort_index()
            st.write(timeslice_df)

            st.bar_chart(timeslice_df)

            st.markdown('----')






        #--------------------------------------------------------------
        # Download button
        @st.cache
        def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        csv = convert_df(data)

        # Create df with time and service from db data
        db_df = pd.DataFrame(data,columns=['Zeit','Leistung'])

        # Get the define of services and create service df
        service_list = DEFINES.getServiceList()
        time = db_df['Zeit']
        _df = pd.DataFrame(columns=service_list)
        _df.insert(loc=0,column='Zeit',value=time)
        service_df = pd.DataFrame(_df)
        st.markdown('----')
        st.subheader("Leistungsübersicht")

        # put and separete values of service into service df

        for index , row in db_df.iterrows():
            value = str(db_df['Leistung'].iloc[index])
            service_db_value_list =  value.split(';')

            #Wert in Liste suchen und mit X markieren
            for i in service_db_value_list:
                for j in service_list:
                    if(i == j):
                        service_df[i][index] =  1
                        break

        # Get slice of dataframe by date
        service_time_df=service_df.set_index('Zeit')
        timeslice =service_time_df.loc[str(sd):str(ed)]
        timeslice = timeslice.sort_index()
        timeslice = timeslice.groupby(timeslice.index)[service_list].sum()
        st.bar_chart(timeslice[service_list])
        st.subheader("Summe der Leistung im Zeitraum")
        st.write(timeslice)


        st.markdown('----')
        st.subheader("Alle Daten downloaden ")
        st.download_button(
            label="Download",
            data=csv,
            file_name=str(today) + '.csv',
            mime='text/csv',)

        # Daten import 
        # filename = st.text_input('Enter a file path:')
        # try:
        #     with open(filename) as input:
        #         st.text(input.read())
        # except FileNotFoundError:
        #     st.error('File not found.')

        if st.button("Daten anschauen!",key="dw"):
            db = database()
            db_data = db.getAllData()
            st.table(db_data)


    
