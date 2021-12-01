#main.py
# system import
import streamlit as st

# module import
import app1
import app2

st.title("MyBahnhofsmission")

msg="Test App für die Bahnhofsmission in FFM"
st.write(msg)
  
PAGES = {
    "App1": app1,
    "App2": app2
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()