import streamlit as st
import plotly.express as px
print('Hello World')

st.title('Hello World? Title Mode')
st.write('This goes below')

a = st.slider('Select a value')
b = st.slider('Select another value')
st.write(f'multiplying these two bad boys together gives us {a*b}')

px.bar(x=['a', 'b'], y=[a, b])
#%%

#%%
