# Basic Setup 

# pip install fastapi uvicorn langchain-openai faiss-cpu

# ----------------------------------------------------

# Simple FastAPI + OpenAI 

from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()

llm = ChatOpenAI(model="gpt-4o-mini")

@app.get("/ask")
async def ask(query: str):
    response = llm.invoke(query)
    return {"answer": response.content}

# ----------------------------------------------------
# RAG Integration
# step 1 - 

from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embedding = OpenAIEmbeddings()

# Example data (DB / PDF se aayega real me)
texts = [
    "Bank fraud happened in Delhi",
    "Cyber attack detected in XYZ system"
]

vector_db = FAISS.from_texts(texts, embedding)

# step 2 -

retriever = vector_db.as_retriever()
# ----------------------------------------------------

# FastAPI + RAG Flow

from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()

llm = ChatOpenAI(model="gpt-4o-mini")

@app.get("/rag")
async def rag(query: str):
    # 1. Retrieve relevant data
    docs = retriever.get_relevant_documents(query)

    # 2. Context build
    context = ""
    for d in docs:
        context += d.page_content + "\n"

    # 3. Final prompt
    final_prompt = f"""
    Answer based only on the context:
    {context}

    Question: {query}
    """

    # 4. LLM call
    response = llm.invoke(final_prompt)

    return {"answer": response.content}

# Flow - 

#    User Query
#     ↓
#    FastAPI
#     ↓
#    Retriever (Vector DB)
#     ↓
#    Context mila
#     ↓
#    LLM (OpenAI)
#     ↓
#    Final Answer