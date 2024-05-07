import streamlit as st
import numpy as np
import pandas as pd
import time

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
    st.image('image2.jpeg')
with col2:
    st.image('image2.jpeg')

# Showing status : Progress bar and Error message
st.error('login Failed')
st.success('login successful')
st.info('this is info')
st.warning('this is warning')

bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)


# User input
