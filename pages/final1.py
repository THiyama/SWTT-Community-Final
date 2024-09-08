import streamlit as st

from utils.utils import display_page_titles_sidebar
from utils.designs import display_problem_statement, apply_default_custom_css


HINT_TEXT1 = "ヒント1: 「追憶の港」"
HINT_TEXT2 = "ヒント2: 「港の本性」"
HINT_TEXT3 = "ヒント3: 「その港へ・・・」"
display_page_titles_sidebar()
apply_default_custom_css()

st.header("運命の暗号", divider="rainbow")
display_problem_statement("""
                          <span font-size:45px;">次のヒントをもとに、呪文を導き出せ！</span>
                          """)

hint = st.radio("ヒント", [HINT_TEXT1, HINT_TEXT2, HINT_TEXT3])

if hint == HINT_TEXT1:
    st.image("pages/resources/hint1.png")

if hint == HINT_TEXT2:
    st.image("pages/resources/moscone_center2.png")

if hint == HINT_TEXT3:
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
