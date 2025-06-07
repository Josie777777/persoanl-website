import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h2>Josie Qiu</h2>
        <p>Recent Master's Graduate in Marketing<br>
        The Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:1155215997@link.cuhk.edu.hk">1155215997@link.cuhk.edu.hk</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a 2025 graduate with a dual bachelor's degree in German and Business Administration from Shanghai International Studies University and the University of Bayreuth. I am currently pursuing a Master of Science in Marketing at The Chinese University of Hong Kong.

        Throughout my academic and professional journey, I have consistently demonstrated strong analytical and communication skills, particularly in the field of marketing. My internship experiences at Philips, Yum China (KFC), Envista, and IPSOS have equipped me with practical expertise in consumer research, data analysis, project management, and digital marketing. I am proficient in tools such as Python, Excel, and various data visualization platforms, and I have a proven ability to work effectively in cross-functional and multicultural teams.

        With fluency in English and German, and a solid foundation in both quantitative and qualitative research, I am eager to contribute to a forward-thinking organization where I can apply my skills and continue to grow professionally. 
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R, SQL
        - Technical Skills: Excel (Vlookup, Pivot Table), Word, PPT, Outlook, Pr, Ps
        - Languages: Mandarin, English, German
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 