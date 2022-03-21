import streamlit as st
# import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print('Hello World')

st.title('Hello World? Title Mode')
st.write('This goes below')

a = st.slider('Select a value')
b = st.slider('Select another value')
st.write(f'multiplying these two bad boys together gives us {a*b}')

ab = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')
st.write(ab.head())

sns.hisplot(ab['Quantity'])
plt.show

#%%
