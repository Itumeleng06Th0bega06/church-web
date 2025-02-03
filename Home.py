import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="SBOI", page_icon='assets/Shekinah_logo.png')

# Load CSS
with open('css.py', 'r') as f:
    exec(f.read())

# Constants
LOGO_PATH = "assets/Shekinah_logo.png"
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

'Heavenly Father, We stand before You as a church, united in purpose and committed to Your vision. We dedicate the new season of this ministry to You. Guide us as we navigate this journey with faith and dedication.
"""

def show_logo():
    st.image(LOGO_PATH, use_container_width=True)

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
                show_logo()
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
                with col4:
                    if st.button("Gentlemen", use_container_width=True):
                        st.session_state.index = "Gentlemen"

                if st.session_state.index == "Children":
                    st.markdown("<h1><center>Kingdom minded Kids</center></h1>", unsafe_allow_html=True)
                    st.markdown("<h4><center>Every Saturday @ 9am</center></h4>", unsafe_allow_html=True)
                    st.image("children/10.jpg", use_container_width=True)
                    vid = open('children/A1.mp4', "rb")
                    st.video(vid.read())
                    images = ['children/1.jpg', 'children/2.jpg', 'children/3.jpg', 'children/4.jpg', 'children/5.jpg', 'children/6.jpg', 'children/7.jpg', 'children/8.jpg', 'children/9.jpg', 'children/11.jpg', 'children/12.jpg', 'children/13.jpg', 'children/14.jpg', 'children/15.jpg', 'children/16.jpg', 'children/17.jpg', 'children/18.jpg', 'children/19.jpg']
                    container = st.empty()
                    index = 0
                    while True:
                        with container:
                            st.image(images[index], use_container_width=True)
                        index += 1
                        if index >= len(images):
                            index = 0
                            break
                        time.sleep(5)
                        container.empty()

                if st.session_state.index == "Youth":
                    st.title('Youth')
                    st.image("assets/y1.png")
                    st.write("**Welcome To Shekinah Blaze Outreach International Youth, Where We Are Nurtured To Being God Fearing Kingdom Leaders Through The Unwavering Teachings Of Biblical Principles. Titus 2:1**")
                    st.write("**About Us__Shekinah Blaze Is A Youth Group For Teens And Young Adults. Our Mission Is To Extend God's Love And Teachings To The Unchurched, Empower Young Believers To Love Jesus Boldly And To Provide A Safe Space For Them To:**")
                    st.write("**:orange[. Live By Faith]**")
                    st.write("**:orange[. Build Meaningful Relationships]**")
                    st.write("**:orange[. Develop Leadership Skills]**")
                    st.write("**:orange[. Engage In Community Service]**")
                    st.write("**:orange[. And Lastly Have Fun]**")
                    st.image("assets/y2.png")
                    st.write("**:orange[EMPOWERED BY GOD, ENERGIZED BY COMMUNITY]**")
                    st.write("It’s all about BELONGING… To your FAMILY... To your CHURCH FAMILY... To the FAMILY OF GOD")
                    st.image("assets/y3.png")
                    st.image("assets/y4.jpg")

                if st.session_state.index == "Women":
                    st.title('Women')

                if st.session_state.index == "Gentlemen":
                    st.title("Gentlemen")
                    st.image("assets/mens conference.jpg")
        with tab3:
            st.write(":orange[Key duties of every Church member:]")
            st.write("""
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
growth, health, and mission of the Church community]
""")

Home()
