import streamlit as st
import requests

st.title("🏀 Sports Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Talk sports with me...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    res = requests.post("https://your-api-url/chat", json={"message": user_input})
    print("DEBUG:", res.status_code, res.text)  # Add this line
    bot_reply = res.json()["response"]

    st.session_state.history.append({"role": "bot", "content": bot_reply})

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
