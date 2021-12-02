# erfassung.py
from person import person 
from database import database
import streamlit as st 

def app():
    st.subheader('Personen erfassen')
    st.write('Hier bitte Geschlecht, Alter und Lebenslage erfassen. Zum übernehmen in die Statistik bitte Button "Übernehmen" drücken.')
    
    # container
    c1, c2, c3= st.columns((1, 1, 1))

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
        

    situation = st.multiselect('Menschen in einer Lebenslage mit ... ',
        [   
        'Aufenthalt',
        'Ausländische Wanderarbeiter', 
        'Kids on Tour ohne Angehörige', 
        'mit sozialen Schwierigkeiten', 
        'finanziellen Schwierigkeiten',
        'psychische Erkrankung',
        'körperliche Erkrankung',
        'Migrationshintergrund',
        'Behinderungen',
        'Reisender',
        'alleinreisenden Kinde(er)'
        ],
        ['Aufenthalt'])

    p = person(gender,age,situation)
    
    person_data = p.getData()
    
    st.subheader('Sie haben fogendes ausgewählt:')
    
    for i in range(len(person_data)):
        st.write(str(person_data[i]))
        
    if st.button("Übernehmen",key=c):
        db = database()
        live = ""
        for n in situation:
            live += ';'+ n
        db.add_persondata(gender,age,live)
        st.text("Werte übernommen!")
    else:
        st.text(" ")