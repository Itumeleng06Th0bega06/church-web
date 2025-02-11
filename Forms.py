import streamlit as st
import sqlite3

conn = sqlite3.connect('my_form.db',check_same_thread=False)
cur = conn.cursor()


def form():
    st.header('orange[Visitation Form')
    st.write("""We're Excited To Have You Fellowship With Us. Please fill The Form To Connect With Us""")
    st.info('Required *')
    with st.form('visitors_form'):
        col1,col2=st.columns(2)
        with col1:
            name=st.text_input('enter Name',placeholder='Name *',label_visibility='hidden')
            email=st.text_input('Email',placeholder='Email',label_visibility='hidden')
            gender=st.radio("Gender *",['Male','Female'],index=None)
            about = st.radio("How Did You Hear About Us",['Social Media','Direct Invitation'],index=None,horizontal=True)
        with col2:
            surname=st.text_input('Surname',placeholder='Surname *',label_visibility='hidden')
            contact=st.text_input("Contact",placeholder='Contact *',label_visibility='hidden')                   
            status=st.radio("Marital Status",['Single','Married'],index=None)
            attendance = st.radio("Have You Visited Our Church Before?",['First Timer','Regular Attendee','Interested In Becoming A Member'],horizontal=True,index=None)
        social = st.selectbox("How Can We Contact You",['Call','WhatsApp','Facebook'],placeholder='Options',index=None)
        st.text('We want To Make Sure We Provide The Best Service To Each Guest, Your Suggestions Are Greatly Appreciated, Please Use The Comment Section Below To Comment On Our Service.')
        comments = st.text_area('Comments',placeholder='Comments',label_visibility='hidden')
        submit = st.form_submit_button('Submit')

        if submit:
                if name and surname and contact and gender:
                        if contact.isdigit() and len(contact) == 10:
                                data(name,surname,email,gender,contact,status,attendance,about,social,comments)
                                st.write(f"Thank You {name}  {surname}")
                        else:
                              st.write('invalid contact!')        
                else:
                        st.warning('Please fill all the required spaces marked **')
                
            
def data(a,b,c,d,e,f,g,h,i,j):
    cur.execute("""CREATE TABLE IF NOT EXISTS my_table(NAME TEXT,SURNAME TEXT,EMAIL TEXT,GENDER TEXT,CONTACT TEXT,STATUS TEXT,ATTENDANCE TEXT,ABOUT TEXT,SOCIAL TEXT,COMMENTS TEXT);""")
    cur.execute("INSERT INTO my_table VALUES (?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i,j))
    conn.commit()
    conn.close()
    st.success('submited')
    
form()
