import streamlit as st

from utils.utils import display_page_titles_sidebar
from utils.designs import display_problem_statement

display_page_titles_sidebar()


st.header("運命の暗号", divider="rainbow")
display_problem_statement("次のヒントをもとに、呪文を導き出せ！")

hint = st.radio("ヒント", ["ヒント1", "ヒント2", "ヒント3"])

if hint == "ヒント1":
    st.image("pages/resources/hint1.png")

if hint == "ヒント2":
    st.image("pages/resources/moscone_center.png")

if hint == "ヒント3":
    st.image("pages/resources/hint3.png")

answer = st.text_input("導き出した呪文を入力してください")
if st.button("アタック！", type="primary"):
    if answer == "20250602":
        st.snow()
        if st.button("次の問題に挑戦する"):
            st.switch_page("pages/final2.py")
        
        st.success("正解だ！来年の Snowflake Summit は、2025年6月2日、モスコーンセンターにて開催される！")

    else:
        st.error("残念！不正解だ。")
