from openai import OpenAI
import streamlit as st
import time

st.title("ChatGPT-like clone")

client = OpenAI(api_key="asda")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_response():
    response = ["hi ", "how ", "are ", "u ", "? "]

    for r in response:
        time.sleep(1)
        yield r

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = get_response()
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})