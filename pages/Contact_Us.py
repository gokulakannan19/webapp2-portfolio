import streamlit as st
from send_email import send_email


st.header("Contact Me")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Message")
    message = f"""\
Subject: Portfolio Email

From: {user_email}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
