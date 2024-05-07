import streamlit as st
import pandas as pd

df = pd.read_csv('startup_cleaned.csv')
# Data Cleaning -> Missing values should be taken care of:
df['investors'] = df['investors'].fillna('Undisclosed')


def load_investor_details(investor_):
    st.title(selected_investor)
#     recent 5 investments of investor
    last5_df = df[df['investors'].str.contains(investor_)].head(5)[['startup','vertical','city','round','amount']]
    st.subheader('Recent 5 Investments')
    st.dataframe(last5_df)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    st.title("Overall Analysis")
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Startup Details')
    st.title("Startup Analysis")

else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Investor Details')
    if btn2:
        load_investor_details(selected_investor)



