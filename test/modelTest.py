import time
import os
from dotenv import load_dotenv

from langchain_together import ChatTogether
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
import chromadb

load_dotenv()


model_path = os.environ["MODEL_PATH"]
start_time = time.time()

llm = ChatTogether(model="meta-llama/Llama-Vision-Free", top_p=0.7)

client = chromadb.PersistentClient()

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    collection_name="next_js_documents",
    client=client,
)

context_question = """Given a chat history and the latest user question "
"which might reference context in the chat history, "
"formulate a short consise standalone question with one sentence which can be understood "
"without the chat history. Do NOT answer the question, "
"just reformulate it. If needed and otherwise return it as is."""
context_question_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(context_question),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

query_generator_chain = create_history_aware_retriever(
    llm=llm, retriever=vector_store.as_retriever(), prompt=context_question_prompt
)
