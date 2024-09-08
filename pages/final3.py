import streamlit as st

from utils.utils import display_page_titles_sidebar
from utils.designs import display_problem_statement, apply_default_custom_css

apply_default_custom_css()
st.header("最後の詠唱", divider="rainbow")
display_page_titles_sidebar()
display_problem_statement("""
    <div style="font-size:32px;">
        SnowVillage の村民から手に入れた呪文<br><span style="color:#FF5733; font-size:45px;">「クリスタル・フレア」</span>で<br>
        <span style="color:#29B5E8; font-size:45px;"><strong>クリスタル</strong></span> を復活させろ！
    </div>
""")

