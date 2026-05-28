from langchain_community.llms import Ollama

llm = Ollama(
    model="phi3:latest",
    temperature=0
)


def summarize_text(text):

    # Limit transcript size
    text = text[:12000]

    prompt = f"""
    Summarize this YouTube video transcript.

    Provide:

    1. Overall Summary
    2. Key Points
    3. Important Insights

    Keep the response concise and structured.

    Transcript:
    {text}
    """

    response = llm.invoke(prompt)

    return response