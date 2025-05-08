import streamlit as st

# Set page config
st.set_page_config(page_title="Futuristic Login", layout="centered")

# Custom futuristic CSS
st.markdown("""
    <style>
    body {
        background-color: #0f2027;
        background-image: linear-gradient(315deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 3em;
        text-align: center;
        padding: 20px;
        color: #00ffe1;
        text-shadow: 0 0 10px #00ffe1;
    }
    .stTextInput > div > div > input {
        background-color: #1c1c1c;
        color: #00ffe1;
        border: 1px solid #00ffe1;
    }
    .stButton > button {
        background-color: #00ffe1;
        color: black;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #00bfa5;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<div class="title">🔐 Futuristic Login</div>', unsafe_allow_html=True)

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login logic (simple validation for demo)
if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Welcome, Commander.")
    else:
        st.error("Access Denied. Invalid Credentials.")
