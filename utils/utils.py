import streamlit as st


def display_page_titles_sidebar():
    with st.sidebar:
        st.page_link("app.py", label="選ばれし者の道", icon="🔮")
        st.page_link("pages/final1.py", label="運命の暗号", icon="🌍️")
        st.page_link("pages/final2.py", label="真実の呪文", icon="📜")
        st.page_link("pages/final3.py", label="最後の詠唱", icon="🗣️")

