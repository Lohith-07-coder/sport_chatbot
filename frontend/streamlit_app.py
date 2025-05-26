import streamlit as st
import requests

st.title("🏀 Sports Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Talk sports with me...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    res = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input, "user_id": "fan123"})
    bot_reply = res.json()["response"]
    st.session_state.history.append({"role": "bot", "content": bot_reply})

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
