import streamlit as st
import uuid
import time
from llms import chat

st.title('Chat con LLMs')


messages = st.container(height=300)
if query_user := st.chat_input("preguntame algo"):
    messages.chat_message("user").write(query_user)
    messages.chat_message("assistant").write(chat(query_user))