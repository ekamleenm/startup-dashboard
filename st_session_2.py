import streamlit as st

email = st.text_input('Enter Email')
password = st.text_input('Enter Password')

btn = st.button('Login Here')

if btn:
    if email == 'ekm9@sfu.ca' and password == '1234':
        st.success('Login successful')
    else:
        st.error('Login failed')
