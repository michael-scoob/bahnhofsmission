# erfassung.py

from backend.person import person as person
from backend.database import database
from backend.defines import DEFINES
import streamlit as st 
import datetime

db = database()

def app():

    st.subheader('Personen erfassen')
    st.write('Hier bitte Geschlecht, Alter und Lebenslage erfassen. Leistungen können seperat erfasst werden. \
        \
        Zur Übernahme aller Daten in die Statistik bitte Button "Übernehmen" drücken. \
        Sie haben die Möglichkeit auch nur die erbrachte Leistung zu übernehmen. Hier für bitte "Nur Leistung übernehmen" drücken.')
    
    # container
    c1, c2 = st.columns((1, 1))

    c = c1
    gender = ""
    c.genre = c.radio("Geschlecht", ('Mann', 'Frau', 'Divers'),key=c)
    if c.genre == 'Mann':
        gender = 'Mann'
        c.write('Mann.')
    elif c.genre == 'Frau':
        gender = 'Frau'
        c.write('Frau.')
    elif c.genre == 'Divers':
        gender = 'Divers'
        c.write('Divers.')
    
    c = c2
    age=""
    c.genre = c.radio("Alter", ('unter 18', 'bis 27 (incl.)', 'bis 65 (inclk.)','über 65'),key=c)
    if c.genre == 'unter 18':
        age='unter 18'
        c.write('unter 18')
    elif c.genre == 'bis 27 (incl.)':
        age='bis 27 (incl.)'
        c.write('bis 27 (incl.)')
    elif c.genre == 'bis 65 (inclk.)':
        age='bis 65 (inclk.)'
        c.write('bis 65 (inclk.).')
    elif c.genre == 'über 65':
        age='über 65'
        c.write('über 65')
        
    person_atribute_list=DEFINES.getPersonAtributeList()
    situation = st.multiselect('Die Person befindet sich in den folgenden Lebenslage(n) ... ',
        person_atribute_list,
        ['mit sozialen Schwierigkeiten'],key=11)

    service_list = DEFINES.getServiceList()
    service = st.multiselect('Wir haben folgende Leistung erbracht ... ',
        service_list,
        ['Aufenthalt'],key=22)

    p = person(gender,age,situation,service)
    
    person_data = p.getData()
    
    st.subheader('Sie haben fogendes ausgewählt:')
    
    for i in range(len(person_data)):
        msg = str(person_data[i])
        msg = msg.replace("[]","")
        st.info(str(msg))
        
    c3, c4 = st.columns((1, 1))    
    
    if c3.button("Übernehmen",key=c):
        
        live = ""
        service_data = ""
        for n in situation:
            live += ''+ n + ';'
        for n in service:
            service_data += ''+ n + ';'
            
        time = str(datetime.date.today())
        db.add_persondata(time,gender,age,live,service_data)
        c3.success("Werte übernommen!")
    else:
        st.text(" ")
        
    if c4.button("Nur Leistung übernehmen",key=c):
        gender=";"
        age=";"
        live = ";"
        service_data = ""

        for n in service:
            service_data += ''+ n + ';'
        time = str(datetime.date.today())    
        db.add_persondata(time,gender,age,live,service_data)
        c4.success("Leistung übernommen!")
    else:
        st.text(" ")