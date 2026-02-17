import streamlit as st


with st.form("login form"):
    username = st.text_input("username")
    pasword = st.text_input("password",type="password")
    submitted = st.form_submit_button("Login")

    if submitted :
        st.success(f"Welcome,{username} !")
