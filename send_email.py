import os
import smtplib
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = st.secrets["USERNAME"]  # Replace with your actual Gmail username
    password = st.secrets["PASSWORD"] # Replace with your Gmail app password (not your regular password)
    # Create a secure SSL context
    context = ssl.create_default_context()
    receiver = st.secrets["RECEIVER"]  # Replace with the recipient's email address

    try:
        # Connect to the SMTP server using SMTP_SSL
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            st.info("Email sent successfully")

    except Exception as e:
        st.error(f"Error sending email: {e}")
