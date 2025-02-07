import streamlit as st

with st.form('form',enter_to_submit=False,clear_on_submit=True):

                                st.header('Visitation Form')
                                st.markdown("""**We're Excited To Have You Fellowship With Us. Please fill The Form To Connect With Us**""")
                                st.text('required *')
                                col1,col2=st.columns(2)
                                with col1:
                                        name=st.text_input('First Name',placeholder='First Name *',label_visibility='hidden')
                                        email=st.text_input('Email',placeholder='Email',label_visibility='hidden')
                                        gender=st.radio("Gender *",['Male','Female'],index=None)
                
                                with col2:
                                        surname=st.text_input('Surname',placeholder='Surname *',label_visibility='hidden')
                                        number=st.number_input("Contact",step=1,placeholder='Contact *',label_visibility='hidden',value=None)
                                        status=st.radio("Marital Status *",['Single','Married'],index=None)
                
                                att=st.radio("Have You Visited Our Church Before?",['First Timer','Regular Attendee','Interested In Becoming A Member'],horizontal=True,index=None)
                                about=st.radio("How Did You Hear About Us",['Social Media','Direct Invitation'],index=None,horizontal=True)
                                social_opt=st.multiselect("How Can We Contact You",['Facebook','WhatsApp','Sms'],placeholder='Select One Or More Options')
                                comments=st.text_area('We want To Make Sure We Provide The Best Service To Each Guest, Your Suggestions Are Greatly Appreciated, Please Use The Comment Section Below To Comment On Our Service.',placeholder='Comments')
                                st.text("Please Make Sure The Information Is Correct Before Submitting!!!")
                                submit=st.form_submit_button('Submit')
                                if submit:
                                        if name and surname and number and gender and status:
                                                st.success('Submitted')
                                                st.write('Thank You!')
                                                st.write(name,surname,)
                                        else:
                                                st.error('Please Fill All The Required Fields Marked With *')