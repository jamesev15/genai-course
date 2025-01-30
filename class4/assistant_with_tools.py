from openai import OpenAI
import streamlit as st
import os
from base_agent import agent_executor

st.title("ChatGPT")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        agent_output = agent_executor.invoke({"input": st.session_state.messages[-1]})
        response = st.write(agent_output["output"])

    st.session_state.messages.append({"role": "assistant", "content": agent_output["output"]})