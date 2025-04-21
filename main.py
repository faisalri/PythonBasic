import streamlit as st
import this
import codecs

# Add sidebar with dropdown menu
menu = st.sidebar.selectbox("Menu", ["Home", "About me"])

if menu == "Home":
    st.title("My First WebApp")
    st.divider()

    zen_of_python = codecs.decode(this.s, "rot_13")

    # Menampilkan teks Zen of Python
    st.markdown(f"```\n{zen_of_python}\n```")

    # Add button
    if st.button("Read motivational message"):
        st.write("Consistency is key; keep learning, keep growing until you master it!")

    # Add input text
    name = st.text_input("Write your Name:")
    if name:
        st.write(f"Hi, {name}! Thank you for visiting my first Streamlit app.\n - Faisal")

    # Add image
    st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", caption="Logo Python")

    # Add slider
    age = st.slider("Choose your age:", 0, 100, 25)
    st.write(f"Your age is: {age}")

elif menu == "About me":
    st.title("About Me")
    st.write("Find me at:")

    linkedin_url = "https://www.linkedin.com/in/faisalriyadi/"
    github_url = "https://github.com/faisalri"

    st.markdown(f"""
    <a href="{linkedin_url}" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="50"></a>
    <a href="{github_url}" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="50"></a>
    """, unsafe_allow_html=True)
