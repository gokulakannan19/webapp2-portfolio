import streamlit as st

# Education Page
st.title("🎓 Education")

# Degree 1 - Bachelors
with st.expander("🎓 Bachelor of Science in Computer Science | St. Josephs's College"
                 " | 2016 - 2019"):
    st.markdown("""
    - **Specialization:** Software Development
    - **Key Courses:** Data Structures, Web Development, Database Management  
    - **Final Year Project:** Developed a Full-Stack Web App with Django & React  
    - **Achievements:** Ranked in the Top 5% of the class, Led Coding Club  
    - **Grade:** **A+**  
    """)

# Higher Secondary Education
with st.expander("🏫 Higher Secondary Education | Jegan Matha Matriculation Higher Sec School"
                 " | 2014 - 2016"):
    st.markdown("""
    - **Stream:** Science (Physics, Chemistry, Mathematics, Computer Science)  
    - **Key Subjects:** Mathematics, Computer Science, Physics  
    - **Grade:** **89%**  
    - **Achievements:** Top performer in Computer Science, Represented school in coding competitions  
    """)
