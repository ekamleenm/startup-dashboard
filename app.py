import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')

df = pd.read_csv('startup_cleaned.csv')
# Data Cleaning -> Missing values should be taken care of:
df['investors'] = df['investors'].fillna('Undisclosed')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


def load_overall_analysis():
    st.title("Overall Analysis")
    col1, col2, col3 = st.columns(3)
    # total invested amount
    with col1:
        total_amount = round(df['amount'].sum())
        st.metric("Total Amount", str(total_amount) + ' Crs')

    #     Max Investment made in a startup
    with col2:
        max_amount = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
        st.metric("Max Investment Amount", str(max_amount) + ' Crs')

    with col3:
        avg_amount = round(df.groupby('startup')['amount'].sum().mean())
        st.metric("Average Amount", str(avg_amount) + ' Crs')

    st.header("MoM Graph")
    temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig, ax = plt.subplots()
    ax.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig)


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

    with col2:
        vertical_series = df[df['investors'].str.contains(investor_)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index)
        st.pyplot(fig1)

    df['year'] = df['date'].dt.year
    yoy = df[df['investors'].str.contains(investor_)].groupby('year')['amount'].sum()
    st.subheader('Year on Year Investments')
    fig2, ax2 = plt.subplots()
    ax2.plot(yoy.index, yoy.values)
    st.pyplot(fig2)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    btn0 = st.sidebar.button('Overall Analysis')
    if btn0:
        load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Startup Details')
    st.title("Startup Analysis")

else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Investor Details')
    if btn2:
        load_investor_details(selected_investor)
