import streamlit as st
from generate_mess import generate_chat_response

st.title("Echo Bot")

if "messages" not in st.session_state:
	# 辞書形式で定義
    st.session_state["messages"] = []

if "pre_id" not in st.session_state:
    st.session_state["pre_id"] = None

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("何か質問はありませんか?"):

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_chat_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})