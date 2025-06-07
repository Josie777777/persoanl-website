import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Consumer Marketing Shaving Team Intern
    **Philips, Shenzhen** | *November 2024 - April 2025*
    
    - Managed multiple Portfolio Life Cycle projects. Created 20+ briefs and regularly communicated with different parties to ensure project completion
    - Independently organized the workshop for new function claims, including consumer research, process development, coordinating with different parties, hosting the workshop, claim development and verification, to support key innovation projects
    - Utilized Python and Octopus to collect customer feedback on e-commerce platforms about Philips and competitors’ products and summarized the results to the team
    - Regularly tracked Low-End Shaving range KPI (R&R, CSG, iGM). Analyzed the data and provided summaries
    """)
    
    st.markdown("""
    ### KFC Cob Marketing Intern
    **YumChina, Shanghai** | *May 2024 - August 2024*
    
    - Managed influencers on TikTok and RedNote for multiple projects, e.g. Briefing, KOL screening, 80+ content optimizin, reaching view count around 65k+ and effectively enhancing new products’ awareness
    - Participated in pre-launch proposal meetings and PPMs for Crispy Fried Chicken and Kizza. Put forward creative social media activities and OTV shooting ideas, partly being adopted and implemented 
    - Utilized Excel pivot table and vlookup to update data on KFC's long term chicken product to analyze business performance, subsequently producing and presenting 10+ weekly and monthly reports
    - Gathered information on marketing campaigns of competitors and summarized strengths and weaknesses of their strategies, putting forward marketing optimization plans for KFC's fried chicken products
    """)
    
    st.markdown("""
    ### Dexis Marketing Intern
    **Envista, Shanghai** | *July 2022 - December 2022*
    
    - Curated several dental exhibitions, including the design of event process, cross-departmental communication of promotional materials, exhibition setup and coordination, reaching an average of 50+ intended cooperations, while promoting the communication of the dental industry
    - Independently managed 2 online dental training programs, including collecting and analyzing participants' needs, communicating with experts on themes, contents and schedules, effectively shaping the brand's professionalism and increasing the client's lifecycle value by about 13%
    - Responsible for the operations of WeChat and TikTok accounts. Produced and launched videos and images to drive social media engagement, reaching 16k views daily and a 110% increase in followers
    """)
    
    st.markdown("""
    ### Social Listening and Analytics Intern
    **IPSOS, Shanghai** | *July 2021 - October 2021*
    
    - Utilized Python to track consumers' discussion hotspots on social platforms, reviews on e-commerce platforms and offline shopping experience. Summarized into PPT and made presentations weekly.
    - Analyzed and visualized market trends in beverage industry from annual reports of Nongfu Spring and Chi Forest.
    - Collected innovative brand marketing activities to produce the monthly marketing activity analysis report
    """)
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Research on Impulsive Consumption of JD Users",
            "description": "Used Logistic Regression PRedictive Model to process JD users' Data, and utilized RFM-Model and A/B Test to prodive platform with better strategies.",
            "skills": ["Python", "Logistic Regression", "RFM Model", "A/B Test"]
        },
        {
            "title": "Analytics on Disneyland's Marketing Path on Social Media",
            "description": "Scaped data from Rednote and Douyin, and processed the data with Python to analyze the marketing path of one SH Disneyland's successful campaign, concluding it's effect.",
            "skills": ["Python", "Octoparse"],
        },
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL
        - **Video and Editing Tools:** Adobe Premiere Pro (Pr), Adobe Photoshop (Ps)
        - **Office Skills:** Excel (Vlookup, Pivot Table), Word, PPT, Outlook
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Languages:** Fluent English (IELTS 7.5, GMAT 710) and German
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring teammates
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 