import streamlit as st

from utils.utils import display_page_titles_sidebar
from utils.designs import apply_default_custom_css, display_applied_message


TEAM_ID = "Final_Problem"

display_page_titles_sidebar()

st.title("💎データクリスタルの復活")

css_name = apply_default_custom_css()
message = f"""
    この旅もいよいよ終盤です。<br>

    <strong>選ばれしものたちよ、いざ最後の挑戦に立ち向かうのです！</strong>
    """

display_applied_message(message, css_name)


st.write("")
placeholder = st.empty()
if placeholder.button("挑戦を開始する"):
    st.switch_page("pages/final1.py")
