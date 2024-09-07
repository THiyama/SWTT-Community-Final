import streamlit as st

from utils.utils import display_page_titles_sidebar
from utils.designs import display_problem_statement

ANSWER_TEXT = "呪文"

st.header("真実の呪文", divider="rainbow")

display_page_titles_sidebar()
display_problem_statement("Snowflakeの村人たちから呪文を聞き出せ！")

st.write("Snowflakeで困ったら助けてくれる村人たちが知ってるぞ")
st.image("pages/resources/snowvillage.png")

answer = st.text_input("聞き出した呪文を入力してください")
if st.button("アタック！", type="primary"):
    if answer == ANSWER_TEXT:
        st.snow()
        if st.button("次の問題に挑戦する"):
            st.switch_page("pages/final3.py")
        
        st.success("正解だ！Snowflakeのことで困ったことがあったら、SnowVillageで何でも聞いてくれよな！")
    
    else:
        st.error("残念！不正解だ。")
