import streamlit as st
import uuid
import time


st.title('Chat')

def generate_answer():
    time.sleep(10)
    return str(uuid.uuid4())

messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"Echo: {generate_answer()}")