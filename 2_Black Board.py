import streamlit as st

# Load CSS
with open('css.py', 'r') as f:
    exec(f.read())

# Constants
LOGO_PATH = "assets/Shekinah_logo.png"
WELCOME_MESSAGE = """**We're Excited To Have You Fellowship With Us. Please fill The Form To Connect With Us**"""
BLACK_BOARD_HEADING = """<center><h3>Welcome To The Black Board</h3></center>"""
BLACK_BOARD_NOTE = """<center>Please Note: All Notifications Will Be Found In This Page!!!</center>"""

def show_form():
    with st.form('form', enter_to_submit=False, clear_on_submit=True):
        st.header('Welcome To Shekinah Blaze Outreach International')
        st.markdown(WELCOME_MESSAGE)
        st.text('required *')
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('First Name', placeholder='First Name *', label_visibility='hidden')
            email = st.text_input('Email', placeholder='Email', label_visibility='hidden')
            gender = st.radio("Gender *", ['Male', 'Female'], index=None)

        with col2:
            surname = st.text_input('Surname', placeholder='Surname *', label_visibility='hidden')
            number = st.number_input("Contact", step=1, placeholder='Contact *', label_visibility='hidden', value=None)
            status = st.radio("Marital Status *", ['Single', 'Married'], index=None)

        att = st.radio("Have You Visited Our Church Before?", ['First Timer', 'Regular Attendee', 'Interested In Becoming A Member'], horizontal=True, index=None)
        about = st.radio("How Did You Hear About Us", ['Social Media', 'Direct Invitation'], index=None, horizontal=True)
        social_opt = st.multiselect("How Can We Contact You", ['Facebook', 'WhatsApp', 'Sms'], placeholder='Select One Or More Options')
        comments = st.text_area('We want To Make Sure We Provide The Best Service To Each Guest, Your Suggestions Are Greatly Appreciated, Please Use The Comment Section Below To Share Any Feedback.')

        st.text("Please Make Sure The Information Is Correct Before Submitting!!!")
        submit = st.form_submit_button('Submit')
        if submit:
            if name and surname and number and gender and status:
                st.success('Submitted')
                st.write('Thank You!')
                st.write(name, surname)
            else:
                st.error('Please Fill All The Required Fields Marked With *')

def show_black_board():
    st.markdown(BLACK_BOARD_HEADING, unsafe_allow_html=True)
    st.markdown(BLACK_BOARD_NOTE, unsafe_allow_html=True)
    st.image("assets/1.jpg")
    st.image("assets/25.jpg")

def Black_Board():
    with st.container():
        tab1, tab2 = st.tabs(['Visitors_Form', 'Anouncements'])
        with tab1:
            show_form()
        with tab2:
            show_black_board()

# st.sidebar.image(LOGO_PATH, width=300)

Black_Board()
