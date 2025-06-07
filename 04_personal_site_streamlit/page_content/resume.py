import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Josie_Qiu_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Josie Qiu")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** 1155215997@link.cuhk.edu.hk
    - **Phone:** (852) 5957 5046
    - **LinkedIn:** [linkedin.com/in/josie-qiu](www.linkedin.com/in/josie-qiu)
    - **GitHub:** [github.com/Josie777777](https://github.com/Josie777777)
    - **Address:** 12 Chak Cheung St., Ma Liu Shui, HKSAR
    """)

    st.header("Professional Experience")
    st.markdown("""
    **Consumer Marketing Shaving Team Intern, Philips**
    - *November 2024 - April 2025*
    - Managed multiple Portfolio Life Cycle projects. Created 20+ briefs and regularly communicated with different parties to ensure project completion
    - Independently organized the workshop for new function claims, including consumer research, process development, coordinating with different parties, hosting the workshop, claim development and verification, to support key innovation projects
    - Utilized Python and Octopus to collect customer feedback on e-commerce platforms about Philips and competitors’ products and summarized the results to the team
    - Regularly tracked Low-End Shaving range KPI (R&R, CSG, iGM). Analyzed the data and provided summaries
    

    **KFC Cob Marketing Intern, YumChina**
    - *May 2024 - August 2024*
    - Managed influencers on TikTok and RedNote for multiple projects, e.g. Briefing, KOL screening, 80+ content optimizin, reaching view count around 65k+ and effectively enhancing new products’ awareness
    - Participated in pre-launch proposal meetings and PPMs for Crispy Fried Chicken and Kizza. Put forward creative social media activities and OTV shooting ideas, partly being adopted and implemented 
    - Utilized Excel pivot table and vlookup to update data on KFC's long term chicken product to analyze business performance, subsequently producing and presenting 10+ weekly and monthly reports
    - Gathered information on marketing campaigns of competitors and summarized strengths and weaknesses of their strategies, putting forward marketing optimization plans for KFC's fried chicken products

    **Dexis Marketing Intern, Envista**
    - *July 2022 - December 2022*
    - Curated several dental exhibitions, including the design of event process, cross-departmental communication of promotional materials, exhibition setup and coordination, reaching an average of 50+ intended cooperations, while promoting the communication of the dental industry
    - Independently managed 2 online dental training programs, including collecting and analyzing participants' needs, communicating with experts on themes, contents and schedules, effectively shaping the brand's professionalism and increasing the client's lifecycle value by about 13%
    - Responsible for the operations of WeChat and TikTok accounts. Produced and launched videos and images to drive social media engagement, reaching 16k views daily and a 110% increase in followers

    **Social Listening and Analytics Intern, IPSOS**
    - *July 2021 - October 2021*
    - Utilized Python to track consumers' discussion hotspots on social platforms, reviews on e-commerce platforms and offline shopping experience. Summarized into PPT and made presentations weekly.
    - Analyzed and visualized market trends in beverage industry from annual reports of Nongfu Spring and Chi Forest.
    - Collected innovative brand marketing activities to produce the monthly marketing activity analysis report
    """)


    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *August 2024 - October 2025*
    - GPA: 3.8/4.0
 
    **Bachelor of Art in German, Double Degree in Business Administration**
    - Shanghai International Studies University
    - University of Bayreuth
    - *Graduated: June 2024* 
    - GPA: 3.78+3.81/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R, SQL
    - **Video and Editing Tools:** Adobe Premiere Pro (Pr), Adobe Photoshop (Ps)
    - **Office Skills:** Excel (Vlookup, Pivot Table), Word, PPT, Outlook
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - Certificate for English Majors Grade Eight and Grade Four
    - Certificate for German Majors Grade Eight and Grade Four
    """)

    st.header("Projects")
    st.markdown("""
    **Research on Impulsive Consumption of JD Users**
    - Used Logistic Regression PRedictive Model to process JD users' Data.
    - Utilized RFM-Model and A/B Test to prodive platform with better strategies.

    **Analytics on Disneyland's Marketing Path on Social Media**
    - Scaped data from Rednote and Douyin.
    - Processed the data with Python to analyze the marketing path of one SH Disneyland's successful campaign, concluding it's effect.
    """)


    st.header("Languages")
    st.markdown("""
    - **English:** Native
    - **German:** Intermediate
    """)

    st.header("Interests")
    st.markdown("""
    - Travelling
    - Photographing and video editting
    """)

    st.markdown("---") 