import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Portfolio", page_icon="👨‍💻", layout="wide")

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("images/Gokulakannan.jpg", width=200)  # Replace with your image file

with col2:
    st.title("👋 Hi, I'm Gokula Kannan!")
    st.subheader("Software Engineer | Python Developer | DevOps Enthusiast")
    st.write("""
    🚀 Passionate about **building scalable applications, automating workflows, and designing cloud-based solutions**.  
    💡 Always eager to learn and apply new technologies to solve real-world problems.  
    """)

st.divider()

# --- ABOUT ME SECTION ---
st.header("🛠 About Me")
st.write("""
With experience in **software development, cloud computing, and DevOps**, my expertise includes:  
✅ **Python** (Django, Flask, Pandas)  
✅ **Cloud Platforms** (AWS)  
✅ **CI/CD Pipelines** (GitHub Actions, GitLab CI/CD)  
✅ **Microservices & REST APIs**  
✅ **Infrastructure as Code (Bash Scripting)**
✅ **Database (MySQL, Postgresql)**  
""")

# --- CONTACT DETAILS ---
# --- CONTACT & SOCIAL DETAILS ---
st.header("📞 Get in Touch")
st.markdown("📞 **Phone:** [+91 9788508844](tel:+1234567890)")
st.markdown("📧 **Email:** [goks.cloud19@gmail.com](mailto:goks.cloud19@gmail.com)")
st.markdown("💻 **GitHub:** [github.com/gokulakannan19](https://github.com/gokulakannan19)")
st.markdown("🔗 **LinkedIn:** [linkedin.com/in/gokulakannan19](https://linkedin.com/in/gokulakannan19)")

# # --- GET IN TOUCH SECTION ---
# st.header("📬 Get in Touch")
#
# with st.form("contact_form"):
#     name = st.text_input("Your Name")
#     email = st.text_input("Your Email")
#     message = st.text_area("Your Message")
#
#     submitted = st.form_submit_button("Send Message")
#     if submitted:
#         st.success("Thank you! I'll get back to you soon. 😊")
