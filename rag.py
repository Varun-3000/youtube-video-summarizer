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
from langchain.text_splitter import RecursiveCharacterTextSplitter

llm = Ollama(model="gemma:2b")


def summarize_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    chunk_summaries = []

    for chunk in chunks:

        prompt = f"""
        Summarize this part of a YouTube video transcript:

        {chunk}

        Give concise bullet points.
        """

        response = llm.invoke(prompt)

        chunk_summaries.append(response)

    combined_summary = "\n".join(chunk_summaries)

    final_prompt = f"""
    Combine these summaries into:

    1. Overall Summary
    2. Key Points
    3. Important Insights

    Summaries:
    {combined_summary}
    """

    final_response = llm.invoke(final_prompt)

    return final_response