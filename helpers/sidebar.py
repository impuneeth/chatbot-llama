import streamlit as st
from pypdf import PdfReader

from .initialiseApp import reset_app


def sidebar_component():

    with st.sidebar:
        if st.button(":arrow_left: Back to Home"):
            st.switch_page("Home.py")

        st.container(height=30, border=False)

        input_document = st.file_uploader(
            "Upload Your document here",
            accept_multiple_files=False,
            type=[".txt", ".pdf"],
        )
        if input_document != None:

            if st.button("Submit", use_container_width=True, type="primary"):

                if input_document.type == "text/plain":
                    st.session_state["input_file_data"] = [
                        input_document.read().decode()
                    ]
                    st.session_state["input_file_name"] = input_document.name

                elif input_document.type == "application/pdf":
                    st.session_state["input_file_data"] = []

                    pdf_doc = PdfReader(input_document)
                    for page_number in range(pdf_doc.get_num_pages()):
                        st.session_state["input_file_data"].append(
                            pdf_doc.pages[page_number].extract_text()
                        )
                    st.session_state["input_file_name"] = input_document.name

                else:
                    st.error("Unsupported Document type")

        st.container(height=50, border=False)

        if st.button("Clear Session"):
            reset_app()
            st.rerun()
