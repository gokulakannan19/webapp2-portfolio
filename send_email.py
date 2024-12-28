import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "####"  # Replace with your actual Gmail username
    password = os.getenv("APP_PASSWORD") # Replace with your Gmail app password (not your regular password)
    # Create a secure SSL context
    context = ssl.create_default_context()
    receiver = "####"  # Replace with the recipient's email address

    try:
        # Connect to the SMTP server using SMTP_SSL
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")
