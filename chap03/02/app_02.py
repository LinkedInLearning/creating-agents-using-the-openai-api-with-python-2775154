import streamlit as st
import time 

#if st.button("Click me!"):

# テキスト入力ボックス
text_input = st.text_input("Input", "テキストを入力してください")
# テキストエリア
text_area = st.text_area("Text Area", "テキストを入力してください")

if st.button("回答"):
    with st.spinner("回答を生成中・・・"):
        time.sleep(3)
        st.write("終了")