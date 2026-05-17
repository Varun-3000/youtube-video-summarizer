import streamlit as st
from transcript import get_transcript
from rag import summarize_text

st.set_page_config(page_title="YouTube Video Summarizer")

st.title("YouTube Video Summarizer")
st.write("Summarize any YouTube video using Whisper + Ollama")

url = st.text_input("Enter YouTube Video URL")


if st.button("Generate Summary"):

    if url.strip() == "":
        st.warning("Please enter a valid URL")

    else:

        try:

            with st.spinner("Downloading audio and generating transcript..."):

                transcript = get_transcript(url)

            st.subheader("Transcript")

            st.write(transcript)

            with st.spinner("Generating summary using Ollama..."):

                summary = summarize_text(transcript)

            st.subheader("AI Summary")

            st.write(summary)

        except Exception as e:

            st.error(f"Error: {str(e)}")