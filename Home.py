import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="SBOI",
                   page_icon='assets/Shekinah_logo.png')

# Opening a .py file as css
with open('css.py', 'r') as f: exec(f.read()) 




# Tracking Variable
# Initializing the state of the Main pages



#defining the pages
def Home():
        with st.container():
                tab1,tab2,tab3 = st.tabs(['Home','Ministries',"Church Members"])
                with tab1:
                        with st.container():
                                
                                st.logo("assets/Shekinah_logo.png")
                                st.image("assets/Shekinah_logo.png",use_container_width=True)
                                st.title(":orange[Lord Remember Me]")
                                
                                st.write("Judges 16:28")
                                st.image("assets/25.2.jpg",use_container_width=True)
                                st.markdown("<h1><center>Welcome To Shekinah Blaze Outreach International</center></h1>",unsafe_allow_html=True)
                                st.markdown("""<center>A Church With A Family Concept.</center>""",unsafe_allow_html=True)
                                st.image('assets/25.jpg',use_container_width=True)
                                st.image('assets/15.jpg',use_container_width=True)
                                st.markdown("""<h4><center>Apostle & Prophetess: Mosokini</center></h4>""",unsafe_allow_html=True)
                                st.image("assets/J.png")
                                "---"
                                st.write("""**:orange[Church Covenant]**

Having been led, as we believe, by the Spirit of God to receive the Lord Jesus 
Christ as our Savior; and on the profession of our faith, having been baptized in the 
name of the Father, and of the Son, and of the Holy Spirit, we do now in the 
presence of God, angels and this assembly, most solemnly and joyfully enter into 
covenant with one another, as one body in Christ.

We engage therefore, by the aid of the Holy Spirit, to walk together in Christian 
love; to strive for the advancement of this church in knowledge and holiness; to 
give it a place in our affections, prayers and services above every organization of 
human origin; to sustain it's worship, ordinances discipline and doctrine; to 
contribute cheerfully and regularly, as God has prospered us, towards it's expenses, 
of the support of a faithful and evangelical ministry among us, the relief of the 
poor and the spread of the Gospel throughout the world. In case of difference of 
opinion in the church, we will cheerfully recognize the right of the majority to 
govern.

We also engage to maintain family and secret devotion; to study diligently the 
Word of God; to continually educate our children; to seek the salvation of our 
kindred and acquaintance; to walk circumspectly in the world; to be kind to those 
in our employ, and faithful in the service we promise others; endeavoring in the 
purity of heart and good will towards all men to exemplify and commend our holy 
faith.

We further engage to watch over, to pray for, to exhort and stir up each other 
unto every good word and work; to guard each other's reputation, not needlessly 
exposing the infirmities of others; to participate in each other's joys, and with 
tender sympathy bear one another's burdens and sorrows; to cultivate Christian 
courtesy; to be slow to give or take offense, but always ready for reconciliation, 
being mindful of the rules of the Savior in the eighteenth chapter of Matthew, to 
secure it without delay; and through life, amid evil report, and good report, to seek 
to live to the glory of God, who hath called us out of darkness into His marvelous 
light.

When we remove from this place, we engage as soon as possible to unite with 
some other church where we can carry out the spirit of this covenant and the 
principles of God's Word.
""")                            
                                "---"
                                st.write(":orange[VISION DECLARATION]")
                                st.write("'We commit to nurturing God-Fearing Kingdom Leaders through the unwavering teachings of Biblical Principles, empowering them to fulfill the Great Commission. We dedicate ourselves to reaching the unchurched, guiding them into a life of discipleship, and equipping them to make disciples of others. With faith, unity, and passion, we declare that the best is yet to come. Together, we will take the vision further and glorify God in all we do. We boldly declare in the name of Jesus Christ. Amen' ")
                                ":orange[VISION DEDICATION]"
                                "'Heavenly Father, We stand before You as a church, united in purpose and committed to Your vision. We dedicate the new season of this ministry to You. Guide us as we nurture God-Fearing kingdom Leaders and extend Your love to the unchurched. Empower us with wisdom, strength and courage to fulfill this calling. May this vision ignite passion in eery heart, and may Your Spirit lead us in every decisiom and step we take. Let Your will be done in us and through us for Your glory. In the mighty name of Jesus Christ we pray. Amen.'"
                                "---"
                                st.info("DO YOU WANT TO LEARN MORE ABOUT THE VISION! VISIT THE (ABOUT) PAGE IN THE SIDE-BAR MENU")
                                

                        
                with tab2:
                        if "index" not in st.session_state:
                                st.session_state.index = "Children"
                        with st.container():
                                col1,col2,col3,col4=st.columns(4)
                                "```"
                                with col1:
                                        if st.button("Children",use_container_width=True):
                                                st.session_state.index = "Children"
                                        
                                with col2:
                                        if st.button('Youth',use_container_width=True):
                                                st.session_state.index = "Youth"
                                                
                                with col3:
                                        if st.button("Women",use_container_width=True):
                                                st.session_state.index = "Women"
                                        
                                with col4:
                                        if st.button("Gentlemen",use_container_width=True):
                                                st.session_state.index = "Gentlemen"
                                        
                        
                        # displaying the contents
                                if st.session_state.index == "Children":                                                            
                                        st.markdown("""<h1><center>Kingdom minded Kids</center></h1>""",unsafe_allow_html=True)
                                        st.markdown("""<h4><center>Every Saturday @ 9am</center></h4>""",unsafe_allow_html=True)
                                        "---"
                                        st.image("children/10.jpg",use_container_width=True)                 
                                        st.markdown("""<h4><center>Our goal at Shekinah Blaze is to introduce children to Jesus at each phase of life so they can have a close relationship with Him. Our leaders aim to provide fun, safe and engaging lessons as they bring the bible to life.</center></h4>""",unsafe_allow_html=True)
                                        "---"
                                        
                                        vid = open('children/A1.mp4',"rb")
                                        st.video(vid.read())
                                #Image Slideshow
                                        
                                        images = ['children/1.jpg','children/2.jpg',
                                          'children/3.jpg','children/4.jpg',
                                          'children/5.jpg','children/6.jpg',
                                          'children/7.jpg','children/8.jpg',
                                          'children/9.jpg','children/11.jpg',
                                          'children/12.jpg','children/13.jpg',
                                          'children/14.jpg','children/15.jpg',
                                          'children/16.jpg','children/17.jpg',
                                          'children/18.jpg','children/19.jpg']
                                        container = st.empty()
                                        index = 0
                                        while True:
                                                with container:
                                                        with st.container(border = True):
                                                                st.image(images[index],use_container_width=True)
                                                        index += 1
                                                        if index >= len(images):
                                                                index = 0
                                                                break
                                                        time.sleep(5)
                                                        container.empty()
                                
                                

                        
                                if st.session_state.index == "Youth":
                                        
                                        st.title('Youth')
                                        st.image("assets/y1.png")
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
                                        st.image("assets/y2.png")
                                        "**:orange[EMPOWERED BY GOD, ENERGIZED BY COMMUNITY]**"
                                        """It’s all about BELONGING…
To your FAMILY...
To your CHURCH FAMILY...
To the FAMILY OF GOD"""
                                        st.image("assets/y3.png")
                                        st.image("assets/y4.jpg")
                                        
                                        "```"
                                        
                                if st.session_state.index == "Women":
                                        st.title('Women')
                                        



                                if st.session_state.index == "Gentlemen":
                                        st.title("Gentlemen")
                                        st.image("assets/mens conference.jpg")
                                with tab3:
                                        "```"
                                        st.write(""":orange[Key duties of every Church member:]
1. Attending Services Regularly
Make it a priority to attend church services consistently, participating in worship, teachings, 
and fellowship with other believers to grow spiritually.

2. Engaging in Personal Spiritual Growth
Commit to personal spiritual practices such as prayer, Bible study, and seeking God’s 
guidance, nurturing a relationship with God beyond just attending services.


3. Serving in Church Ministries
Volunteer in church ministries according to individual gifts and talents, contributing to the 
Church’s mission and supporting others within the community.

4. Supporting the Church Vision and Leadership
Align with the Church’s vision and uphold respect for its leaders, encouraging unity, 
supporting initiatives, and contributing to the church’s goals.

5. Giving Financially and Generously
Contribute financially through tithes and offerings to support the Church’s operations, 
missions, and outreach programs, giving as an act of worship and stewardship.

6. Participating in Fellowship and Building Community
Build relationships with other Church members, engaging in fellowship, small groups, or 
Church events, fostering a strong, supportive Christian community.

7. Living as a Positive Example
Live a life that reflects Christian values in personal conduct, relationships, and decision making, being a witness to others both inside and outside the Church.

8. Evangelizing and Inviting Others
Share the gospel and invite others to Church, helping to spread God’s Word and welcome 
new believers into the community.

9. Praying for the Church and its Members
Pray regularly for the Church’s vision, leadership, ministries, and fellow members, 
interceding for God’s guidance, protection, and blessing over the Church.

10. Upholding Unity and Avoiding Conflict
Promote unity by resolving conflicts respectfully, speaking positively about the Church, and 
avoiding gossip or divisive behavior, fostering peace within the Church family.

:orange[These duties enable each Church member to actively contribute to the 
growth, health, and mission of the Church community]""")
                        
                        
                        
                   
st.sidebar.image("assets/Shekinah_logo.png")

Home()



                    
                               
          





    
