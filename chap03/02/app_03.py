import streamlit as st
import time
 
with st.form("my_form", clear_on_submit=False):
    name = st.text_input('名前を入力してください')
    options = st.multiselect(
        "見たい競技は何ですか",
        ["サッカー", "バレーボール", "陸上", "卓球", "柔道"],
        #default=['Yellow', 'Red'] # デフォルトの設定
    )
    description = st.text_area("詳細な希望を入力してください")
    submitted = st.form_submit_button("スケジュールを立てる")
     
     
if submitted:
    with st.spinner("スケジュールを立てる..."):
        time.sleep(3)
    st.subheader(name + "様")
    st.text(description)  
    st.text("あなたの旅行計画はこれです！")