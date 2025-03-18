import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

# @st.cache_data
# def get_data():
#     return pd.DataFrame(np.random.randn(20000, 2), columns=["x", "y"])

@st.cache_resource
def get_time():
    # graph = g.compile()
    return datetime.now()

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(get_data(), x="x", y="y", color=color)
st.write(get_time())
st.slider("he")