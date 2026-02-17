import streamlit as st

# Hardcoded credentials (for demo only)
VALID_USERNAME = "nachiket"
VALID_PASSWORD = "1234"

st.title("Simple Login App")

# Create session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

else:
    st.write(f"Hello {st.session_state.username} 👋")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
