#main.py
# system import
import streamlit as st

# module import
import erfassung as erfassung
import statistik as statistik
from auth import auth

# page setup

st.set_page_config(
    page_title="Bahnhofsmission",
    page_icon="🧊",
    layout= "wide" ,#"centered", #"wide",
    initial_sidebar_state="expanded",
    )

#Logo at sidebar
#st.sidebar.image('./pic/kisspng-bahnhofsmission-mnchen-hauptbahnhof-diakonia-old-5b2c64b9ce7e02.1766947615296360258458.png',width=3,use_column_width=True)


# st.sidebar.title("Meine Bahnhofsmission")
# msg="Anwendung für Bahnhofsmissionen um \
#     die Besucher und die vermittelten Leistunge zur erfassen \
#     und statistisch auszuwerten."    
# st.sidebar.write(msg)

# st.sidebar.markdown('----')

c1, c2 = st.sidebar.columns(2)
c2.metric(label="Temperatur", value="13 °C", delta="1.2 °C")
c1.image('./kisspng-bahnhofsmission-mnchen-hauptbahnhof-diakonia-old-5b2c64b9ce7e02.1766947615296360258458.png',width=3,use_column_width=True)
st.sidebar.markdown('----')
# add pages here
PAGES = {
    "Erfassen"  : erfassung,
    "Statistik" : statistik
}

# Page: Home


# Login
a=auth()
login_status = a.auth_run()

if a.getLoginStatus() == True:
    # navigation to page
    #st.markdown("_____")

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio(" ", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    
    #st.markdown("_____")