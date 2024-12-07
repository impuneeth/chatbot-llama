import streamlit as st


def initialise_app():

    if "input_file_data" not in st.session_state.keys():
        st.session_state["input_file_data"] = False
        st.session_state["input_file_name"] = ""

    if "chat" not in st.session_state.keys():
        st.session_state["chat"] = [
            {
                "role": "assistant",
                "content": "Ask questions about your document",
            }
        ]

    if "chat_history" not in st.session_state.keys():
        st.session_state["chat_history"] = []


def intialise_next_chatapp():
    if "nx_chat" not in st.session_state.keys():
        st.session_state["nx_chat"] = [
            {
                "role": "assistant",
                "content": "Hello! How can I help you today?",
            }
        ]

    if "nx_chat_history" not in st.session_state.keys():
        st.session_state["nx_chat_history"] = []


def reset_app():

    st.session_state["input_file_data"] = False
    st.session_state["input_file_name"] = ""
    st.session_state["chat"] = [
        {
            "role": "assistant",
            "content": "Ask questions about your document",
        }
    ]
    st.session_state["chat_history"] = []


def nx_reset_app():
    st.session_state["nx_chat"] = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?",
        }
    ]
    st.session_state["nx_chat_history"] = []
