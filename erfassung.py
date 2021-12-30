# erfassung.py

from backend.person import person as person
from backend.database import database
from backend.defines import DEFINES
import streamlit as st 
import datetime

db = database()

def app():

    st.subheader('Besucher erfassen')
    st.write('Hier bitte für Besucher das Geschlecht, Alter und Lebenslage erfassen. \
        Leistungen können seperat erfasst werden. \
        \
        Zur Übernahme aller Daten in die Statistik bitte Button "Übernehmen" drücken. \
        Sie haben die Möglichkeit auch nur die erbrachte Leistung zu übernehmen. Hier für bitte "Nur Leistung übernehmen" drücken.')
    
    # container
    c1, c2 = st.columns((1, 1))

    c = c1
    gender = ""
    gender_list = DEFINES.getGenderList()
    c.value = c.radio("Geschlecht", (gender_list),key='cg')
    gender = c.value

    c = c2
    age = ""
    age_list = DEFINES.getAgeList()
    c.value = c.radio("Alter Test", (age_list),key='ag')
    age = c.value

    person_atribute_list=DEFINES.getPersonAtributeList()
    situation = st.multiselect('Die Person befindet sich in den folgenden Lebenslage(n) ... ',
        person_atribute_list,
        key=11)

    service_list = DEFINES.getServiceList()
    service = st.multiselect('Wir haben folgende Leistung(en) erbracht ... ',
        service_list,
        key=22)

    p = person(gender,age,situation,service)
    
    person_data = p.getData()
    
    st.subheader('Sie haben fogendes ausgewählt:')
    
    for i in range(len(person_data)):
        msg = str(person_data[i])
        msg = msg.replace("[]","")
        st.info(str(msg))
        
    c3, c4 = st.columns((1, 1))    
    
    if c3.button("Übernehmen",key=c):
        time = str(datetime.date.today())
        time+=""
        gender+=""
        age+=""
        live = ""
        service_data = ""

        if len(situation) != 0:
            for n in situation:
                live += ''+ n + ';'
        else:
            live += ""

        if len(service) != 0:
            for n in service:
                service_data += ''+ n + ';'
        else:
            service_data += ""

        db.addDataToTable(time,gender,age,live,service_data)
        c3.success("Werte übernommen!")
    else:
        st.text(" ")
        
    if c4.button("Nur Leistung übernehmen",key=c):
        time = str(datetime.date.today())
        time+=""
        gender=""
        age=""
        live = ""
        service_data = ""

        for n in service:
            service_data += ''+ n + ';'
           
        db.addDataToTable(time,gender,age,live,service_data)
        c4.success("Leistung übernommen!")
    else:
        st.text(" ")