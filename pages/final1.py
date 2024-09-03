import streamlit as st

from utils.utils import display_page_titles_sidebar


display_page_titles_sidebar()

if "unmei_is_clear" not in st.session_state:
    st.session_state.unmei_is_clear = False


st.header("運命の暗号", divider="rainbow")
answer = st.text_input("回答を入力してください")
if st.button("アタック！", type="primary"):
    if answer == "20250602":
        st.success("正解だ！来年の Snowflake Summit は、2025年6月2日、モスコーンセンターにて開催される！")
        st.snow()
        st.session_state.unmei_is_clear = True
    else:
        st.error("残念！不正解だ。")

if st.session_state.unmei_is_clear:
    if st.button("次の問題に挑戦する"):
        st.switch_page("pages/final2.py")

if st.toggle("ヒントを表示する"):
    st.image("pages/resources/moscone_center.png")
