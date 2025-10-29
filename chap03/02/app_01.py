#
# streamlitのインスト－ル
# pip install streamlit
#
# アプリの実行
# streamlit run app.py
# 
# 停止
# Ctrl+c

import streamlit as st # 別名をstにすることが多い

# タイトル
st.title("streamlitのページ")
# ヘッダー
st.header("header")
# サブヘッダー
st.subheader("subheader")
# テキスト
st.text("text")
# st.write()はMarkdown対応
st.write("# headline1")
st.write("## headline1")
st.write("### headline1")

# 明示的にmarkdown記法
st.markdown("# Hello, streamlit!")
