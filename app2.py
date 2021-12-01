# app2.py
import streamlit as st
import datetime
def app():
    st.title('APP2')
    st.write('Welcome to app2')
    d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)
    