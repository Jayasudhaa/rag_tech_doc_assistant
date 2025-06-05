import os
import openai
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import TextLoader

import streamlit as st

documents = []

docs_path = "docs"
for filename in os.listdir(docs_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(docs_path, filename)
        loader = TextLoader(file_path)
        documents.extend(loader.load())

#----Step 1: Load Docs--
loader = DirectoryLoader("docs", glob = "**/*.txt.", use_multithreading = True)
documents = loader.load()


#---Step 2: Split into Chunks---
splitter = RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap= 50)
chunks = splitter.split_documents(documents)

st.write(f"Loaded {len(documents)} documents")
st.write(f"Split into {len(chunks)} chunks")

#---Step 3: Generate Embeddings ---
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

#---Step 4: Setup Retrieval Chain--
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever = retriever)

#---Step 5:Streamlit UI ---
st.title("RAG Technical Assistant")
query = st.text_input("Ask me anything from the docs:")

if query:
    result = qa_chain.run(query)
    st.write("**Answer:**", result)