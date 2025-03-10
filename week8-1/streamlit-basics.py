import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
  'id': [1, 2, 3, 4],
  'scores': [10, 20, 30, 40]
})

st.write(df)

st.dataframe(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])


st.line_chart(chart_data)

lat_min, lat_max = -18.0, -0.0
lon_min, lon_max = -81.35, -68.65

# Generate random latitude and longitude values within Peru
map_data = pd.DataFrame({
    'lat': np.random.uniform(lat_min, lat_max, 1000),
    'lon': np.random.uniform(lon_min, lon_max, 1000)
})

st.map(map_data)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

