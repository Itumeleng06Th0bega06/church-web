import streamlit as st

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
LOGO_PATH = "assets/Shekinah_logo.png"
VISION_TEXT = """
Raising God Fearing Kingdom Leaders
By Teaching Uncompromised Bible
Principles.
"""
MISSION_TEXT = """
To Reach The Unchurched
Through Discipleship.
"""
CHURCH_OBJECTIVES = [
    """•The Church aims to raise God fearing Leaders in every community that the 
    Church operates in. Leadership without the fear of GOD leads to 
    selfishness and corruption.""",
    """•Members of the Church need to demonstrate GOD fearing characters in 
    every area of their lives. Members have to be selfless in their service for 
    the Master(Jesus Christ).""",
    """•Members have to demonstrate the love of God towards fellow members 
    and the community at large. We can’t be happy to sleep with full stomachs 
    while our fellow members go hungry and while our neighbors sleep on 
    empty stomachs. We have to care for and love each other and our 
    community. The Church will help eradicate poverty in the communities by 
    planting vegetable gardens to help distribute fresh vegetable hampers to 
    the needy within our communities.""",
    """•The Church will be involved in crime prevention initiatives and in playing 
    an active role in assisting to rehabilitate ex-offenders by teaching sound 
    Biblical values and by assisting to re-incorporate them back to their 
    communities. The Church will also provide spiritual counseling to the 
    inmates.""",
    """•The Church will also be involved in hospital Ministry by visiting hospitals to pray for 
    the sick and providing spiritual guidance to the sick. The Church intends to build a 
    centre for the terminally ill so as to have them close to the Church for prayers and 
    spiritual support. Doctors and nurses will be on hand to provide necessary medical 
    assistance. Trained care-givers will run the centre on a fulltime basis. Pastors and 
    trained counselors will provide counseling on a regular basis.""",
    """•The Church intends to reach out to the prostitution community to lead them to 
    Christ in order to reduce the HIV/AIDS pandemic. The Church will provide counseling 
    and spiritual guidance to those who want to change their ways. The Church will have 
    a shelter for such people who are seeking refuge so as to mend their lives.""",
    """•The Church will have a shelter for the destitute and the abused. The Church will 
    house women and children who need shelter and children until such time that they 
    find homes or places where they can live normal lives. The Church will help look after 
    HIV/AIDS orphans.""",
    """•The Church will raise funds to achieve its objectives through donations from 
    individuals and organizations that share or support our goals. The Church will also 
    raise funds through campaigns and sponsorships from governmental and private 
    institutions."""
]

STATEMENT_OF_FAITH = """
1. We believe that the Scriptures of the Old and New Testament are verbally inspired of God, and they are without          
error in the original writings, and they are the supreme and final authority for faith and life.

2. We believe in one God, Creator and Sustainer of the universe, Who is eternally existent in three persons —
Father, Son, and Holy Spirit.
                        
3. We believe in the Deity of Jesus Christ, His virgin birth, sinless life, His death to pay the penalty for everyone’s 
sins, His bodily resurrection, His exaltation at God’s right hand, and His personal, imminent, pretribulational and 
pre-millennial return.
                        
4. We believe that all have sinned and are therefore guilty before God and are under His condemnation.
                        
5. We believe that all who by faith receive Jesus Christ are born again of the Holy Spirit, therefore children of God 
and eternally saved, and that the Holy Spirit dwells within every believer to enlighten, guide, and enable the 
believer in life, testimony, and service. We believe that God answers the prayers of His people and meets their 
needs according to His purpose.
                        
6. We believe that God gives spiritual gifts to all believers for the building up of the body of Christ. However, the 
miraculous sign-gifts of the Spirit, such as tongues and healings, were limited to the early church.
                        
7. We believe in the bodily resurrection of the just and unjust, the everlasting blessedness of the saved in Glory 
and the everlasting conscious punishment of the lost in hell.
                        
8. We believe that all believers are called to a life of separation from all worldly and sinful practices and alliances.
                        
9. We believe that from the beginning with Adam and Eve, God ordained marriage as only between one man and 
one woman. All sexual activity outside of this biblical definition of marriage, including homosexual practices, is in 
direct contradiction to God’s Word and His intention for the institution of the home.
"""

CORE_VALUES = """
:orange[**Family**]_We believe there is nothing more important 
than strong united families.
                     
**:orange[Excellence]**_We believe excellence honours God and 
inspires greatness.
                         
**:orange[Equipping]**_We believe in equipping the saints for 
ministry and life by helping them to operate in their 
spiritual gifts.

**:orange[Prayer]**_We believe in the power of prayer, and that 
makes a critical difference in all we attempt to achieve. 
We are to be a house of prayer for all nations.
                         
**:orange[Authenticity]**_Through authentic living, biblical 
authority, worship, prayer, and spirit.
                         
**:orange[Committed Community]**_Through intimacy within the 
community, servant leadership, genuine relationships, 
and beauty in diversity.
"""

def About():
    with st.container():
        tab1, tab2 = st.tabs(['Vision And Mission', 'KingDom Leaders'])
        with tab1:
            st.image("assets/l1.jpg", use_container_width=True)
            st.subheader(":orange[Vision.]")
            st.text(VISION_TEXT)
            st.subheader(":orange[Mission.]")
            st.text(MISSION_TEXT)
            "___"

            st.image("assets/l2.jpg", width=800)  # image deco
            for objective in CHURCH_OBJECTIVES:
                st.write(objective)
                
            st.image("assets/l3.jpg", width=800)
            st.image("assets/l4.jpg", width=800)
            st.image("assets/l5.jpg", width=800)

            st.header(":orange[Statement Of Faith]")
            st.write(STATEMENT_OF_FAITH)

            with st.expander("Learn More"):
                st.write(""":orange[Historicity of Genesis]
Word of Life Bible Institute is committed to the historical and factual accuracy of the book of Genesis. Therefore, 
we teach a recent creation of the entire universe and all forms of life in the six, 24-hour days of the creation 
week. We believe that Adam and Eve were the first man and woman and that all of mankind has descended 
from them and has inherited a sin nature from their fall into sin, resulting in a cursed creation. We believe in a 
personal Satan who led some of the angels to rebel, enticed Eve to eat the forbidden fruit, and continues to 
oppose God’s program for human history. We believe in a worldwide flood which explains the disappearance of 
certain species recorded in the fossil record, the subsequent development of mankind from Noah, and the 
creation of language groups and nations from God’s intervention at the Tower of Babel. We believe that Satan’s 
attempt to overthrow God is doomed to fail and that the Lake of Fire has been prepared as a place of eternal 
conscious punishment for him, his demons, and all humans who reject Christ""")
            "___"
            st.image("assets/l6.jpg", width=800)
            st.header(":orange[Core Values]")
            st.markdown(CORE_VALUES)

        with tab2:
            "___"
            st.markdown("<center><h2>Kingdom Leaders</center></h2>", unsafe_allow_html=True)
            st.markdown("<center><h4>Pastoral Team</center></h4>", unsafe_allow_html=True)
            "___"
            # Pastoral Team
            col1, col2 = st.columns(2)
            with col1:
                st.image('assets/Mosokini.png', use_container_width=True)
                st.markdown("**<center>Head Of Pastoral: :orange[Maduo Mosokini]</center>**", unsafe_allow_html=True)
                st.image('assets/Serapane.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[William Serapane]</center>**", unsafe_allow_html=True)
                st.image('assets/Sekgetho.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[Gopolang Sekghetho]</center>**", unsafe_allow_html=True)
                st.image('assets/Esau.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[Tumo Esau]</center>**", unsafe_allow_html=True)

            with col2:
                st.image('assets/Lesetedi.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[Puseletso Lesetedi]</center>**", unsafe_allow_html=True)
                st.image('assets/Lesang.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[Nonofo Lesang]</center>**", unsafe_allow_html=True)
                st.image('assets/Segwai.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[Koketso Segwai]</center>**", unsafe_allow_html=True)
                st.image('assets/Thobega.png', use_container_width=True)
                st.markdown("**<center>Pastor: :orange[Itumeleng Thobega]</center>**", unsafe_allow_html=True)

            st.image("assets/Mr & Mrs.png", width=800)
            st.markdown("""<center><h1>Key duties of an Associate Pastor to support the Visionary Leader</h1></center>
1. Preaching and Teaching Support
Assist in delivering sermons and teaching Bible studies to share the preaching load and 
provide variety in spiritual nourishment. This also includes leading special services when 
needed.
2. Pastoral Care and Counseling
Offer pastoral care through counseling, hospital visits, and support for Church members in 
times of crisis, complementing the efforts of the Visionary Leader and ensuring no one is 
overlooked.
3. Administrative Assistance
Help with the Church's administrative duties, such as overseeing specific ministries, 
organizing events, and managing staff or volunteer schedules, to lighten the Visionary 
Leader's workload.
4. Leadership Development and Mentorship
Mentor and train Church Leaders and volunteers, fostering a culture of growth and 
equipping others for ministry roles, which aligns with the Church’s vision for expanding its 
reach and impact.
5. Supporting the Vision and Strategic Planning
Work closely with the Visionary Leader to understand the Church’s Vision and contribute to 
strategic planning. Help implement initiatives that advance the Mission and maintain unity 
in the Leadership team.
6. Outreach and Community Engagement
Lead or support outreach programs and community involvement, aiming to extend the 
Church's influence beyond its walls. This includes coordinating events or partnerships that 
align with the Church's goals.
7. Worship Service Coordination
Assist in planning and executing worship services, ensuring that all elements (music, 
sermons, announcements) are well-organized and contribute to a cohesive service 
experience.
8. Conflict Resolution and Mediation
Address conflicts or issues within the Church body, providing mediation to maintain unity 
and a healthy Church environment, and alleviating pressure on the Visionary Leader.
9. Prayer Ministry Support
Lead prayer meetings and intercessory ministries to ensure that the spiritual health of the 
congregation is prioritized, supporting the Visionary Leader's focus on spiritual growth.
10. Event Planning and Execution
Assist in organizing and executing Church events, retreats, or conferences that align with 
the church's mission and vision, providing hands-on support to bring the Visionary Leader's 
ideas to life. These duties enable the Associate Pastor to share responsibilities with the Visionary 
Leader, ensuring the Church operates smoothly and continues to grow according to its 
vision.</left>""", unsafe_allow_html=True)

# st.sidebar.image(LOGO_PATH)

# Calling the function
About()
