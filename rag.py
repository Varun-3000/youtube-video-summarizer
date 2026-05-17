# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_ollama import ChatOllama, OllamaEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain.chains import RetrievalQA


# def build_qa_chain(text):

#     # 1. Split transcript
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=200
#     )

#     docs = splitter.create_documents([text])

#     # 2. Embeddings
#     embeddings = OllamaEmbeddings(model="nomic-embed-text")

#     # 3. Vector DB
#     db = Chroma.from_documents(
#         docs,
#         embedding=embeddings,
#         persist_directory="chroma_db"
#     )

#     retriever = db.as_retriever()

#     # 4. LLM
#     llm = ChatOllama(model="llama3")

#     # 5. QA chain
#     qa = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever
#     )

#     return qa
from langchain_community.llms import Ollama


def summarize_text(text):

    llm = Ollama(model="llama3")

    prompt = f"""
    Summarize the following YouTube video transcript.

    Transcript:
    {text}

    Provide:
    1. Short Summary
    2. Key Points
    3. Important Insights
    """

    response = llm.invoke(prompt)

    return response