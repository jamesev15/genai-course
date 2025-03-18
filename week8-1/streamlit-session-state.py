import uuid
import streamlit as st

def save_value():
    print(st.session_state.counter)

if "counter" not in st.session_state:
    st.session_state["counter"] = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")

st.button("Run it again", on_click=save_value)

# if "id" not in st.session_state:
#     st.session_state["id"] = uuid.uuid4()

# st.write(st.session_state["id"])
# st.write("hello")

st.slider("temperature")
# st.write("sdsd")
