import os
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.messages import HumanMessage, AIMessage
from langchain_together import ChatTogether
import streamlit as st

from helpers import sidebar_component, initialise_app

load_dotenv()

st.set_page_config(page_icon="📄", page_title="Chat With your Document")

st.header("Chat with Your Document")


initialise_app()
sidebar_component()

if st.session_state["input_file_data"]:
    st.caption(body="You are now chatting with: " + st.session_state["input_file_name"])


def load_documents():

    if st.session_state["input_file_data"]:
        with st.spinner("Loading Documents, please wait..."):

            docs = st.session_state["input_file_data"]

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=500,
            )
            doc_splits = splitter.create_documents(docs)

            return doc_splits


input_docs = load_documents()


@st.cache_resource()
def load_llm():
    llm = ChatTogether(
        model="meta-llama/Llama-Vision-Free",
        temperature=0.7,
        api_key=st.secrets["api_key"],
    )
    return llm


llm = load_llm()


def retrieve_documents(user_question, chat_history):

    qa = "You are a question answer bot. Only use the Context Documents provided below to answer the user question.\n\nContext Documents:\n{context}"
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(qa),
            MessagesPlaceholder("chat_history"),
            HumanMessagePromptTemplate.from_template("{input}"),
        ]
    )
    doc_reteiver_chain = prompt | llm
    response = doc_reteiver_chain.invoke(
        {"input": user_question, "context": input_docs, "chat_history": chat_history}
    ).content

    return response


if st.session_state["input_file_data"]:
    user_question = st.chat_input(placeholder="Enter your question here")
    if user_question:
        st.session_state["chat"].append({"role": "user", "content": user_question})

    for messages in st.session_state["chat"]:
        st.chat_message(messages["role"]).write(messages["content"])

else:
    st.info(
        "Upload the file you want to chat with in the side bar and submit the file. If you want to start a new chat session, click on 'Clear Session' button and upload a new file."
    )

if st.session_state["chat"][-1]["role"] == "user":
    with st.spinner("Thinking..."):
        response = retrieve_documents(
            user_question, chat_history=st.session_state["chat_history"]
        )
        message = {
            "role": "assistant",
            "content": response,
        }
        st.session_state["chat_history"].extend(
            [
                HumanMessage(content=user_question),
                AIMessage(content=response),
            ]
        )
        st.session_state["chat"].append(message)

    st.chat_message("assistant").write(response)
