import streamlit as st

# --- SKILLS SECTION ---
st.header("💡 Skills")

# Detect Streamlit theme mode (light/dark)
theme = st.get_option("theme.base")
bg_color = "#f4f4f4" if theme == "light" else "#1e1e1e"
text_color = "#000000" if theme == "light" else "#ffffff"
shadow_color = "rgba(0, 0, 0, 0.1)" if theme == "light" else "rgba(255, 255, 255, 0.2)"

# Custom CSS for skill cards
st.markdown(f"""
    <style>
        .skill-card {{
            background-color: {bg_color};
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px {shadow_color};
            color: {text_color};
        }}
        .skill-title {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .emoji {{
            font-size: 24px;
        }}
    </style>
""", unsafe_allow_html=True)

# Skill categories in three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="skill-card"><div class="emoji">🐍</div><div class="skill-title">Python</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🛢️</div><div class="skill-title">SQL</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🎭</div><div class="skill-title">Django</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">☁️</div><div class="skill-title">AWS</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="skill-card"><div class="emoji">🐧</div><div class="skill-title">Linux</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🖥️</div><div class="skill-title">Bash Scripting</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🚀</div><div class="skill-title">Django Rest Framework</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🔗</div><div class="skill-title">Git</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="skill-card"><div class="emoji">🏗️</div><div class="skill-title">OOPS</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🔄</div><div class="skill-title">ORM</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">📊</div><div class="skill-title">Pandas</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-card"><div class="emoji">🐳</div><div class="skill-title">Docker</div></div>', unsafe_allow_html=True)
