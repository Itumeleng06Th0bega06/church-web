import streamlit as st



with st.container():
                                
                                tab1,tab2,tab3,tab4=st.tabs(["Children","Youth","Women","Gentlemen"])
                                                
                                with tab1:
                                                                                                    
                                        st.markdown("""<h1><center>Kingdom minded Kids</center></h1>""",unsafe_allow_html=True)
                                        st.markdown("""<h4><center>Every Saturday @ 9am</center></h4>""",unsafe_allow_html=True)
                                        "```"
                                        st.image("10.jpg",use_container_width=True)                 
                                        st.markdown("""<h4><center>Our goal at Shekinah Blaze is to introduce children to Jesus at each phase of life so they can have a close relationship with Him. Our leaders aim to provide fun, safe and engaging lessons as they bring the bible to life.</center></h4>""",unsafe_allow_html=True)
                                        "```"
                                                
                                        vid = open('A1.mp4',"rb")
                                        st.video(vid.read())
                                        
                                        
                                with tab2:
                                        st.title('Youth')
                                        st.image("y1.png")
                                        """**Welcome To Shekinah Blaze Outreach Internationl Youth, Where We Are Nutured To Being God Fearing Kingdom Learders
                                         Through The Unwavering Teachings Of Biblical Principles. Titus 2:1**"""
                                        """**About Us__Shekinah Blaze Is A Youth Group For Teens And Young Adults.
                                        Our Mission Is To Extend God's Love And Teachings To The Unchurched, Empower Young Believers To Love Jesus boldly And To Provide A Safe Space Them To:**"""
                                        "**:orange[. Live By Faith]**"
                                        "**:orange[. Build Meaningful Relationships]**"
                                        "**:orange[. Develop Leadership Skills]**"
                                        "**:orange[. Engage In Community Service]**"
                                        "**:orange[. And Lastly Have Fun]**"
                                        
                                        "*Our Values*"
                                        "**1. Faith_We Are Committed To Helping Young People To Be Rooted In Their Relationship With Jesus**"
                                        "**2. Inclusivity_We Welcome Everyone Regardless Of Their Background Or Belief.**"
                                        "**3. Community Service_We're Passionate about Being Positively Impactful To The Community**"        
                                        
                                        st.image("y2.png")
                                        "**:orange[EMPOWERED BY GOD, ENERGIZED BY COMMUNITY]**"
                                        """It’s all about BELONGING…
To your FAMILY...
To your CHURCH FAMILY...
To the FAMILY OF GOD"""
                                        st.image("y3.png")
                                        st.image("y4.jpg")
                                        
                                        "```"
                                        
                                                
                                with tab3:
                                        st.title('Women')
                                        st.image("w1.png")
                                        


                                with tab4:
                                        st.title("Gentlemen")
                                        st.image("mens conference.jpg")