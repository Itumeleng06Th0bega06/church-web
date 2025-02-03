import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="SBOI")

# Load CSS
try:
    with open('css.py', 'r') as f:
        css = f.read()
        exec(css)
except FileNotFoundError:
    st.error("CSS file not found.")
except Exception as e:
    st.error(f"An error occurred while loading the CSS: {e}")

# Constants
CHURCH_COVENANT = """
**:orange[Church Covenant]**

Having been led, as we believe, by the Spirit of God to receive the Lord Jesus 
Christ as our Savior; and on the profession of our faith, having been baptized in the 
name of the Father, and of the Son, and of the Holy Spirit, we do now in the 
presence of God, angels and this assembly, most solemnly and joyfully enter into 
covenant with one another, as one body in Christ.

...

When we remove from this place, we engage as soon as possible to unite with 
some other church where we can carry out the spirit of this covenant and the 
principles of God's Word.
"""

VISION_DECLARATION = """
:orange[VISION DECLARATION]

'We commit to nurturing God-Fearing Kingdom Leaders through the unwavering teachings of Biblical Principles, empowering them to fulfill the Great Commission.
"""

VISION_DEDICATION = """
:orange[VISION DEDICATION]

'Heavenly Father, We stand before You as a church, united in purpose and committed to Your vision. We dedicate the new season of this ministry to You. Guide us as we navigate this journey with faith and wisdom. Amen.'
"""

def show_welcome_message():
    st.title(":orange[Lord Remember Me]")
    st.write("Judges 16:28")
    st.image("assets/25.2.jpg", use_container_width=True)
    st.markdown("<h1><center>Welcome To Shekinah Blaze Outreach International</center></h1>", unsafe_allow_html=True)
    st.markdown("<center>A Church With A Family Concept.</center>", unsafe_allow_html=True)
    st.image('assets/25.jpg', use_container_width=True)
    st.image('assets/15.jpg', use_container_width=True)
    st.markdown("<h4><center>Apostle & Prophetess: Mosokini</center></h4>", unsafe_allow_html=True)
    st.image("assets/J.png")
    st.write(CHURCH_COVENANT)
    st.write(VISION_DECLARATION)
    st.write(VISION_DEDICATION)
    st.info("DO YOU WANT TO LEARN MORE ABOUT THE VISION! VISIT THE (ABOUT) PAGE IN THE SIDE-BAR MENU")

def Home():
    with st.container():
        tab1, tab2, tab3 = st.tabs(['Home', 'Ministries', "Church Members"])
        with tab1:
            with st.container():
                show_welcome_message()
        with tab2:
            if "index" not in st.session_state:
                st.session_state.index = "Children"
            with st.container():
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    if st.button("Children", use_container_width=True):
                        st.session_state.index = "Children"
                with col2:
                    if st.button('Youth', use_container_width=True):
                        st.session_state.index = "Youth"
                with col3:
                    if st.button("Women", use_container_width=True):
                        st.session_state.index = "Women"

Home()
