import streamlit as st
import pathlib

# Set up the page
st.set_page_config(page_title="SBOI",
                   layout='centered',
                   page_icon='Shekinah_logo.png')



home = st.Page(
    page="views/Home.py",
    title="Home",
    icon= ":material/play_arrow:",
    
)
pastoral = st.Page(
    page="views/Pastoral Team.py",
    title="Pastoral Team",
    icon= ":material/play_arrow:",
)
ministries = st.Page(
    page="views/Ministries.py",
    title="Ministries",
    icon= ":material/play_arrow:",
)
anouncement = st.Page(
    page="views/Anouncements.py",
    title="Anouncements",
    icon= ":material/play_arrow:",
)

members = st.Page(
    page="views/Members.py",
    title="Members",
    icon= ":material/play_arrow:",
)
v_m = st.Page(
    page="views/Vision And Mission.py",
    title="Vision And Mission",
    icon= ":material/play_arrow:",
)
pages = st.navigation(
    {
        "MAIN MENU": [home,pastoral,ministries],
        "BLACK BOARD": [anouncement],
        "ABOUT": [members,v_m],
        
    }
)
pages.run()


# sidebar logo
st.logo('Shekinah_logo.png',size='large')
st.sidebar.image("Shekinah_logo.png",width=300)

# css file
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("assets/styles.css")
load_css(css_path)

# Hidding Stuff
hide_style = """<style>
            #MainMenu{visibility: visible;}
            footer{visibility: hidden;}</style>"""

st.markdown(hide_style,unsafe_allow_html=True)