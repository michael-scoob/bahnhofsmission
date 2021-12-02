#main.py
# system import
import streamlit as st


# module import
import erfassung
import statistik
from auth import auth

# page setup

st.set_page_config(
    page_title="Bahnhofsmission",
    page_icon="🧊",
    layout="centered", #"wide",
    initial_sidebar_state="expanded",
    )

# add pages here
PAGES = {
    "Erfassen"  : erfassung,
    "Statistik" : statistik
}

# Page: Home
st.title("Meine Bahnhofsmission")
msg="Statistik Anwendung für die Bahnhofsmission in FFM um die Besucher und die vermittelten Leistunge zur erfassen"
st.write(msg)

# Login
a=auth()
login_status = a.auth_run()

if a.getLoginStatus() == True:
    # navigation to page
    st.markdown("_____")

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio(" ", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    st.markdown("_____")