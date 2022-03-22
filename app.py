import streamlit as st
# import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder

print('Hello World')

st.title('Hello World? Title Mode')
st.write('This goes below')

a = st.slider('Select a value')
b = st.slider('Select another value')
st.write(f'multiplying these two bad boys together gives us {a * b}')


@st.experimental_memo
def load_superstore():
    superstore_dud = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')
    return superstore_dud


superstore = load_superstore()
st.write(superstore.head())
fig, ax = plt.subplots()
ax = sns.histplot(superstore['Quantity'])
st.pyplot(fig)
print(superstore.columns)
superstore.dropna(inplace=True)
X = superstore[['Ship Mode', 'Segment', 'Country', 'City', 'State',
                'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
                'Product Name', 'Sales', 'Quantity']]

oe = OrdinalEncoder()
X = oe.fit_transform(X=X)

y = superstore['Profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf = RandomForestRegressor(random_state=35)
rf.fit(X_train, y_train)
print(rf.score(X_train, y_train))
print(rf.score(X_test, y_test))
