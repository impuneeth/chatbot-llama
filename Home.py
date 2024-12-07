import streamlit as st

st.set_page_config(
    page_icon=":house:",
    page_title="Home Page",
    initial_sidebar_state="collapsed",
    layout="wide",
)


st.header(
    "Welcome to Llama Chatbot: AI Assistant for Knowledge and Document Analysis",
    divider="violet",
)


st.container(height=75, border=False)

col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="large")


with col2:
    c = st.container(border=True)
    c.header(" 💬 Ask Anything Chat", divider="violet")
    c.write(
        "Explore topics, get answers, and learn effortlessly with AI. Ask anything and gain insights instantly."
    )
    if c.button("Ask a Question :sparkles:", use_container_width=True):
        st.switch_page("pages/Chat.py")

with col3:
    c = st.container(border=True)
    c.header("📄 Upload & Analyze", divider="violet")
    c.markdown(
        "Upload documents and let AI simplify your analysis. Analyze documents and get answers in seconds."
    )
    if c.button(
        "Analyze Documents :sparkles:", use_container_width=True, key="dochat_button"
    ):
        st.switch_page("pages/docChat.py")
