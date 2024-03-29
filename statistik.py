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
    year=str(datetime.date.year)
    month=str(datetime.date.month)
    day=str(datetime.date.day)
    today = datetime.date.today()
    
    st.subheader("Alle Daten anschauen oder downloaden ")
    c1, c2 , c3 , c4 = st.columns((1, 1, 1, 1)) 
    db = database()
    data = db.getAllData() #methode return a df
    csv = convert_df(data)
    
    if c1.button("Daten anschauen!",key="dw"):
        db = database()
        db_data = db.getAllData()
        st.table(db_data)
        
    c2.download_button(
        label="Download",
        data=csv,
        file_name=str(today) + '.csv',
        mime='text/csv',)
    
    
    
    
    
    
    
    # # Datum auswahl
    # st.subheader("Bitte einen Zeitraum auswählen ...")
    # c1, c2 = st.columns((1, 1)) 
    # sd = c1.date_input("Von ", today,max_value=today,key="sd")
    # ed = c2.date_input("Bis", today,max_value=today,key="ed")

    # if ed < sd:
    #     st.info('Bitte Zeitraum prüfen!')
    # else:
    #     db = database()
    #     data = db.getAllData() #methode return a df 
    
    #     # Personen Statistik
    #     st.markdown('----')  
    #     # people_df = pd.DataFrame(data,columns=['Zeit','Geschlecht','Alter'])
        
        # #--------------------------------------------------------------
        # # Geschlecht abfragen
        # mann = 0
        # frau = 0
        # divers = 0

        # for index, row in people_df.iterrows():
        #     s = str(people_df['Geschlecht'].iloc[index])
        #     if s == ';':
        #         people_df['Geschlecht'].iloc[index] = str(0)
        #     elif s == 'Divers':
        #         divers = divers + 1
        #     elif s == 'Mann':
        #         mann = mann + 1
        #     elif s == 'Frau':
        #         frau = frau + 1
        # # Debug
        # # st.write("Männer: " + str(mann) + " | Frauen: " + str(frau) + " | Divers: " + str(divers))
        
        # #--------------------------------------------------------------
        # # Alter abfrage
        # unter_18 = 0
        # bis_27 = 0
        # bis_65 = 0
        # über_65 = 0

        # for index, row in people_df.iterrows():
        #     s = str(people_df['Alter'].iloc[index])
        #     if s == 'unter 18':
        #         unter_18 = unter_18 + 1
        #     elif s == 'bis 27 (incl.)':
        #         bis_27 = bis_27 + 1
        #     elif s == 'bis 65 (inclk.)':
        #         bis_65 = bis_65 + 1
        #     elif s == 'über 65':
        #         über_65 = über_65 + 1
        #     else: 
        #         people_df['Alter'].iloc[index] = str('0')
        # # Debug
        # # st.write("unter 18: " + str(unter_18) + " | bis 27: " + str(bis_27) + " |  bis 65: " + str(bis_65) + " | über 65: " + str(über_65))
        
        #--------------------------------------------------------------
        # Besucher
        # st.title("Besucher gesamt" )
        # time = [str(sd)]
        # people_list=[]
        # people_list.append([mann,frau,divers])
        # people_list_df = pd.DataFrame(people_list,columns=['Männlich', 'Weiblich','Divers'])
        
        
        # people_list_df.insert(loc=0,column='Zeit',value=time)
        # people_list_df = people_list_df.set_index('Zeit')
        # st.bar_chart(people_list_df)
        # st.write(people_list_df)
        
        # st.markdown('----')
        # #--------------------------------------------------------------
        # # Altersgruppen
        # st.title("Altersgruppen")
        # age_list=[]
        # age_list.append([unter_18,bis_27,bis_65,über_65])
        # age_list_df = pd.DataFrame(age_list,columns=['unter 18', 'bis 27','bis 65','über 65'])

        # age_list_df.insert(loc=0,column='Zeit',value=time)
        # age_list_df = age_list_df.set_index('Zeit')
        # st.bar_chart(age_list_df)
        # st.write(age_list_df)
        
        # #--------------------------------------------------------------
        
        # # Create df with time and service from db data
        # db_df = pd.DataFrame(data,columns=['Zeit','Leistung'])
        # csv = convert_df(data)
        # # Get the define of services and create service df
        # service_list = DEFINES.getServiceList()
        # time = db_df['Zeit']
        # _df = pd.DataFrame(columns=service_list)
        # _df.insert(loc=0,column='Zeit',value=time)
        # #st.write(_df)
        # service_df = pd.DataFrame(_df)
        # st.markdown('----')
        # st.title("Leistungsübersicht")

        # # put and separete values of service into service df
        # for index , row in db_df.iterrows():
        #     value = str(db_df['Leistung'].iloc[index])
        #     service_db_value_list =  value.split(';')

        #     #Wert in Liste suchen und mit X markieren
        #     for i in service_db_value_list:
        #         for j in service_list:
        #             if(i == j):
        #                 service_df[i][index] =  1
        #                 break

        # # Get slice of dataframe by date
        # service_time_df=service_df.set_index('Zeit')
        # timeslice =service_time_df.loc[str(sd):str(ed)]
        # timeslice = timeslice.sort_index()
        # timeslice = timeslice.groupby(timeslice.index)[service_list].sum()
        # # st.bar_chart(timeslice[service_list])
        # st.bar_chart(service_time_df)
        # st.subheader("Summe der Leistung im Zeitraum")
        # st.write(service_time_df)

        #st.markdown('----')
        # st.subheader("Alle Daten anschauen oder downloaden ")
        # c1, c2 , c3 , c4 = st.columns((1, 1, 1, 1)) 
        # db = database()
        # data = db.getAllData() #methode return a df
        # csv = convert_df(data)
        
        # if c1.button("Daten anschauen!",key="dw"):
        #     db = database()
        #     db_data = db.getAllData()
        #     st.table(db_data)
          
        # c2.download_button(
        #     label="Download",
        #     data=csv,
        #     file_name=str(today) + '.csv',
        #     mime='text/csv',)

        # Daten import 
        # filename = st.text_input('Enter a file path:')
        # try:
        #     with open(filename) as input:
        #         st.text(input.read())
        # except FileNotFoundError:
        #     st.error('File not found.')