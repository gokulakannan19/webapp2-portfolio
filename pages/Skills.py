import streamlit as st

# --- SKILLS SECTION ---
st.header("💡 Skills")

# Custom CSS for skill cards
st.markdown("""
    <style>
        .skill-card {
            background-color: #f4f4f4;
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .skill-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .emoji {
            font-size: 24px;
        }
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
