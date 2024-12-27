import streamlit as st

st.header("Contact Me")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    message = st.text_area("Message")
    button = st.form_submit_button("Submit")
    if button:
        print(button)
        print("I am pressed")

