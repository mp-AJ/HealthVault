import streamlit as st

# Page config
st.set_page_config(page_title="Stylish Login", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    body {
        margin: 0;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 95vh;
        background: linear-gradient(to top right, #00c6ff, #0072ff);
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }
    .login-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 2em;
        border-radius: 20px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
        text-align: center;
        width: 90%;
        max-width: 400px;
    }
    .profile-pic {
        border-radius: 50%;
        width: 100px;
        margin-bottom: 15px;
    }
    .input-style input {
        width: 100%;
        padding: 0.75em;
        margin: 10px 0;
        border: none;
        border-radius: 25px;
        background-color: white;
        color: black;
        font-size: 1em;
    }
    .login-button {
        background-color: black;
        color: white;
        padding: 0.75em;
        width: 100%;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        cursor: pointer;
    }
    .login-button:hover {
        background-color: #333;
    }
    .footer {
        margin-top: 1em;
        font-size: 0.85em;
        color: #eee;
    }
    </style>
""", unsafe_allow_html=True)

# HTML layout
st.markdown("""
    <div class="container">
        <div class="login-box">
            <img src="https://randomuser.me/api/portraits/women/44.jpg" class="profile-pic">
            <h3>John Doe</h3>
            <div class="input-style">
                <form action="#" method="post">
                    <input name="username" placeholder="Username" type="text" />
                    <input name="password" placeholder="Password" type="password" />
                    <button class="login-button" type="submit">Login</button>
                </form>
            </div>
            <div class="footer">Forgot Username / Password?</div>
        </div>
    </div>
""", unsafe_allow_html=True)
