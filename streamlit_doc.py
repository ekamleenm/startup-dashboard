import streamlit as st
import pandas as pd

email = st.text_input('Enter Email')
password = st.text_input('Enter Password')
gender = st.selectbox('Select Gender', ['m', 'f', 'other'])

btn = st.button('Login Here')

if btn:
    if email == 'ekm9@sfu.ca' and password == '1234':
        st.success('Login successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login failed')

file = st.file_uploader('Upload a csv File')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('I am loving it')

st.write('this is a normal text')

st.markdown("""
### My Favorite movies 
 - abc
 - def
 - fgh""")

# Code
st.code("""
def foo(input):
    return input**2
        
        
x = foo(2)
""")

# latex
st.latex('x^2 + y^2 + 2 = 0')

# Display Elements
df = pd.DataFrame({'name': ['ekam', 'shaina', 'gurnaj'],
                   'age': [22, 21, 15],
                   'gender': ['f', 'f', 'm']
                   })

st.dataframe(df)

# metrics
st.metric('Revenue', '$ 3000', '-3%')

st.json(df.to_dict(orient='records'))

# Display media
# st.image('image2.jpeg')


# Creating layouts
st.sidebar.code("""
def foo(input):
    return input**2
        
        
x = foo(2)
""")

#
col1, col2 = st.columns(2)

with col1:
    st.image('#')
with col2:
    st.image('#')

# Showing status : Progress bar and Error message
st.error('login Failed')
st.success('login successful')
st.info('this is info')
st.warning('this is warning')

bar = st.progress(0)
for i in range(100):
    bar.progress(i)

# User input
# text input
email = st.text_input('enter email')
number = st.number_input('enter age')
date = st.date_input('enter date')
