#main.py
# system import
import streamlit as st

# module import
import app1
import app2

# page setup

#st.set_page_config(layout="wide")
PAGES = {
    "Erfassen"  : app1,
    "Statistik" : app2
}

# Page: Home
st.title("Meine Bahnhofsmission")
msg="Statistik Anwendung für die Bahnhofsmission in FFM um die Besucher und die vermittelten Leistunge zur erfassen"
st.write(msg)

# navigation to page
st.markdown("_____")

st.sidebar.title('Navigation')
selection = st.sidebar.radio(" ", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.markdown("_____")