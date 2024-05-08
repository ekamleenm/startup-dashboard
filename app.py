import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')

df = pd.read_csv('startup_cleaned.csv')
# Data Cleaning -> Missing values should be taken care of:
df['investors'] = df['investors'].fillna('Undisclosed')


def load_investor_details(investor_):
    st.title(selected_investor)
    #     recent 5 investments of investor
    last5_df = df[df['investors'].str.contains(investor_)].head(5)[['startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Recent Investments')
    st.dataframe(last5_df)
    col1, col2 = st.columns(2)
    with col1:
        #     Biggest 5 investments
        big_series = df[df['investors'].str.contains(investor_)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head(5)
        st.subheader('Top Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)


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
