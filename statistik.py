# statistik.py
import streamlit as st
import datetime
import pandas as pd
import numpy as np
from backend.database import database

def app():
    st.title('Statistik')
    st.write('Auswertung der Daten über auszuwählende Zeiträume. Bitte einen Zeitraum wählen!')
    d = st.date_input("Datum wählen", datetime.date(2019, 7, 6))
    st.write('Ausgewältes Datum ist:', d)
    
    # st.title('Demo Daten')
    # chart_data = pd.DataFrame(  
    # np.random.randn(20, 3),
    # columns=['a', 'b', 'c'])
    # st.line_chart(chart_data)

    if st.button("Daten anschauen!",key=d):
        db = database()
        db_data = db.getAllData()
        st.table(db_data)


    
