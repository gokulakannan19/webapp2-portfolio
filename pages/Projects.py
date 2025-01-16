import streamlit as st

# --- PROJECTS PAGE ---
st.header("🚀 My Projects")

# Sample project data (replace with your actual projects)
projects = [
    {
        "title": "E-commerce Platform",
        "image": "images/1.png",  # Replace with actual image URL or local path
        "source_code": "https://github.com/yourusername/ecommerce-platform",
        "live_demo": "https://your-ecommerce-app.com"
    },
    {
        "title": "AI Chatbot",
        "image": "images/2.png",
        "source_code": "https://github.com/yourusername/ai-chatbot",
        "live_demo": None  # No live demo available
    },
    {
        "title": "Portfolio Website",
        "image": "images/3.png",
        "source_code": "https://github.com/yourusername/portfolio",
        "live_demo": "https://yourportfolio.com"
    }
]

# Display projects in columns
for project in projects:
    st.subheader(project["title"])

    # Display project image
    st.image(project["image"], use_container_width=True)

    # Source code button
    st.markdown(f"[🔗 Source Code]({project['source_code']})", unsafe_allow_html=True)

    # Live demo button (if available)
    if project["live_demo"]:
        st.markdown(f"[🌐 Live Demo]({project['live_demo']})", unsafe_allow_html=True)

    st.write("---")  # Divider between projects
