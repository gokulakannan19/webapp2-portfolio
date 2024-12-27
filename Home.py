import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/Gokulakannan.jpg")

with col2:
    st.title("Gokula Kannan")
    content1 = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    st.info(content1)

content2 = """
Below you can find some of the apps i have built in python. Feel free to contact me
"""
st.write(content2)

df = pd.read_csv(r"C:\Users\sanch\PythonProjects\app2-portfolio\data.csv", sep=";")

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