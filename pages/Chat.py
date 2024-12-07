import os
from dotenv import load_dotenv

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import HumanMessage, AIMessage
from langchain_together import ChatTogether
import streamlit as st

from helpers import intialise_next_chatapp, nx_reset_app

load_dotenv()

st.set_page_config(page_icon="💬", layout="centered")

intialise_next_chatapp()

col1, col2 = st.columns([4, 1])

with col1:
    if st.button(":arrow_left: Back to Home"):
        st.switch_page("Home.py")

with col2:
    if st.button("Clear Session"):
        nx_reset_app()
        st.rerun()

st.header("Ask away your questions!!", divider="violet")


@st.cache_resource()
def load_llm():
    llm = ChatTogether(
        model="meta-llama/Llama-Vision-Free",
        top_p=0.7,
        api_key=st.secrets["api_key"],
    )
    return llm


llm = load_llm()


qa_prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

chain = qa_prompt | llm

user_question = st.chat_input(placeholder="Enter your question here")
if user_question:
    st.session_state["nx_chat"].append({"role": "user", "content": user_question})

for messages in st.session_state["nx_chat"]:
    st.chat_message(messages["role"]).write(messages["content"])


if st.session_state["nx_chat"][-1]["role"] == "user":
    with st.spinner("Thinking..."):
        response = chain.invoke(
            input={
                "input": user_question,
                "chat_history": st.session_state["nx_chat_history"],
            }
        )
        message = {
            "role": "assistant",
            "content": response.content,
        }
        st.session_state["nx_chat_history"].extend(
            [
                HumanMessage(content=user_question),
                AIMessage(content=response.content),
            ]
        )
        st.session_state["nx_chat"].append(message)

    st.chat_message("assistant").write(response.content)
