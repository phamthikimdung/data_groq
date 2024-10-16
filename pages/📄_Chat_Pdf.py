import os
import tempfile
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
GROQ_API_KEY = "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"

def load_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        temperature=0.0,
        model_name="llama-3.1-70b-versatile"
    )

def load_document(file_path):
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        return documents
    except Exception as e:
        st.error(f"Error loading document: {e}")
        return []

def setup_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings()
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )
    doc_chunks = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(doc_chunks, embeddings)
    return vectorstore

def create_chain(vectorstore):
    llm = load_llm()
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )
    return chain

st.set_page_config(
    page_title="Simple Q&A with PDF",
    page_icon="📄",
    layout="centered"
)

st.title("🦙 Simple Q&A with PDF")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "conversation_chain" not in st.session_state:
    st.session_state.conversation_chain = None
with st.sidebar:
    uploaded_file = st.file_uploader(label="Upload your PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

    documents = load_document(temp_file_path)
    if documents:
        st.session_state.vectorstore = setup_vectorstore(documents)
        st.session_state.conversation_chain = create_chain(st.session_state.vectorstore)
        st.success("PDF loaded and vectorstore created successfully!")
    else:
        st.error("Failed to load documents. Please check the PDF file.")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask a question about the PDF...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    if st.session_state.conversation_chain:
        with st.chat_message("assistant"):
            response = st.session_state.conversation_chain({"question": user_input})
            assistant_response = response["answer"]
            st.markdown(assistant_response)
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    else:
        st.error("Conversation chain not initialized. Please upload a PDF file.")
