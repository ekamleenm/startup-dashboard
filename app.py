import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding.csv')
st.dataframe(df)

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title("Overall Analysis")
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', ['a', 'b', 'c', 'd'])
    st.title("Startup Analysis")
else:
    st.sidebar.selectbox('Select Investor', ['person1', 'person2', 'person3'])
    st.title("Investor Analysis")
