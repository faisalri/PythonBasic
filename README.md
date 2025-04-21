# My First WebApp

Welcome to my first Streamlit web application! This app demonstrates various features of Streamlit, including text display, buttons, input fields, images, sliders, and a sidebar menu.

## Features

### Home
- **Title and Divider**: Displays the title of the web app and a divider.
- **Zen of Python**: Shows the Zen of Python text.
- **Motivational Message Button**: Click the button to read a motivational message.
- **Name Input**: Enter your name to receive a personalized greeting.
- **Python Logo**: Displays the Python logo.
- **Age Slider**: Choose your age using the slider.

### About Me
- **LinkedIn Icon**: Clickable LinkedIn icon that links to my profile.
- **GitHub Icon**: Clickable GitHub icon that links to my profile.

## How to Run

1. **Install Streamlit**:
    ```bash
    pip install streamlit
    ```

2. **Save the code** in a file named `app.py`:
    ```python
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
        github_url = "https://github.com/faisalriyadi"

        st.markdown(f"""
        <a href="{linkedin_url}" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="50"></a>
        <a href="{github_url}" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="50"></a>
        """, unsafe_allow_html=True)
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

## Contact

Feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/faisalriyr visiting my first Streamlit app! 😊
