import streamlit as st
import pandas as pd
import numpy as np

# df = pd.DataFrame({
#   'id': [1, 2, 3, 4],
#   'scores': [10, 20, 30, 40]
# })

# st.write(df)

# # st.dataframe(df, hide_index=True)

# # chart_data = pd.DataFrame(
# #      np.random.randn(20, 3),
# #      columns=['a', 'b', 'c']
# # )


# # st.line_chart(chart_data)
# #st.write("helloworld2")

# lat_min, lat_max = -18.0, -0.0
# lon_min, lon_max = -81.35, -68.65

# # # Generate random latitude and longitude values within Peru
# # map_data = pd.DataFrame({
# #     'lat': np.random.uniform(lat_min, lat_max, 1000),
# #     'lon': np.random.uniform(lon_min, lon_max, 1000)
# # })

# # st.map(map_data)


# x = st.slider(label='temperature', min_value=10, max_value=100)  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# status_checkbox = st.checkbox('Show dataframe')
# if status_checkbox:
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     st.write(chart_data)

# # df = pd.DataFrame({
# #     'first column': [1, 2, 3, 4],
# #     'second column': [10, 20, 30, 40]
# #     })

# option = st.selectbox(
#     'Which number do you like best?',
#      ["a", "b", "c", "d"])

# st.write('You selected: ', option)

# # import streamlit as st

# text = """# Title
# ## Subtitle
# - hola
# - idat

# """

# #text = """<h1>hello</h1>"""

# st.write(text)

def fn_on_click():
    st.write("hello")

st.button("press me", on_click=fn_on_click)