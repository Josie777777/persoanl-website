import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **The Chinese University of Hong Kong** | *August 2024 - October 2025*
    
    - GPA: 3.8/4.0
    - Relevant Courses: Machine Learning in Marketing, Customer Analytics, Social Media Analytics, Price Analytics, Strategic Brand Management, Buyer Behavior, Marketing Research
    
    ### Bachelor of Art in German, Double Degree in Business Administration
    **Shanghai International Studies University** | *September 2020 - June 2024*
    
    **University of Bayreuth** | *September 2021 - June 2024* 


    - Top 5% in both business and German studies in the double degree structure 
    - Exchange for eight months in Germany, thriving in cross-cultural environment 
    - Relevant Courses: Advanced Maths, Statistics, Python, Microeconomics, Business Finance (all full marks)
    - Scholarship Awards 6 times (top 3%)
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### Certificate for English Majors Grade Eight and Grade Four
        
        Demonstrated expertise in English Listening and Writing.
        """)
        
    with cert2:
        st.markdown("""
        ### Certificate for German Majors Grade Eight and Grade Four
        
        Demonstrated expertise in German Listening and Writing.
        """)
    
    st.markdown("---")
    