import streamlit as st

#
# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
#

st.title("Echo Bot")

if "messages" not in st.session_state:
	# リストの中に辞書形式
    st.session_state["messages"] = []
# チャット履歴を全て表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

print(st.session_state.messages)

# ユーザーの入力を受け取るには、st.chat_inputを使用する 
# st.chat_inputは第一引数にはプロンプト文字列を指定
if prompt := st.chat_input("最近どう?"):

    # ユーザの入力を表示する
    with st.chat_message("user"):
        st.markdown(prompt)
    # ユーザの入力をチャット履歴に追加
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # ChatBotの返答を表示する
    with st.chat_message("assistant"):
        st.markdown(response)
    # ChatBotの返答をチャット履歴に追加
    st.session_state.messages.append({"role": "assistant", "content": response})