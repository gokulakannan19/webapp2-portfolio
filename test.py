import os
import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

image_urls = [
    ("icon/call.png", "9788508855"),
    ("https://example.com/image2.jpg", "https://example.com/link2")
]

col1, col2 = st.columns(2)
with col1:
    st.image("images/Gokulakannan.jpg", width=370)

with col2:
    st.title("Gokula Kannan")
    content1 = """
    Hi, I'm Gokula Kannan, a Software Engineer with 5 years of experience specializing in Python and Django. 
    I'm proficient in Bash scripting, Pandas, and Git, 
    and I'm passionate about building user-friendly and high-performing web applications.

I'm always eager to learn and explore new technologies. 
In my free time, I enjoy gym, watching films.

Feel free to explore some of the projects I've built in Python"""

    st.info(content1)

    st.subheader("📞 Contact")
    st.markdown("""
    - **Phone:** [📞 +91 9788508844]
    - **Email:** [📧 goks.cloud19@gmail.com](mailto:goks.cloud19@gmail.com)
    """)

st.divider()

content2 = """
Below you can find some of the apps i have built in python. Feel free to contact me
"""
st.write(content2)

df = pd.read_csv("data.csv", sep=";")

col3, col4, col5 = st.columns([1.5, 0.5, 1.5])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")