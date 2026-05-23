import streamlit as st
from transcript import get_transcript
from rag import summarize_text
import time

st.set_page_config(page_title="YouTube Video Summarizer")

st.title("YouTube Video Summarizer")
st.write("Summarize any YouTube video using Whisper + Ollama")

url = st.text_input("Enter YouTube Video URL")


if st.button("Generate Summary"):

    if url.strip() == "":
        st.warning("Please enter a valid URL")

    else:

        try:

            total_start = time.time()

            # -------------------------
            # TRANSCRIPTION TIMER
            # -------------------------

            transcription_start = time.time()

            with st.spinner("Downloading audio and generating transcript..."):

                transcript = get_transcript(url)

            transcription_end = time.time()

            transcription_time = round(
                transcription_end - transcription_start,
                2
            )

            st.success(
                f"Transcription completed in {transcription_time} seconds"
            )

            # -------------------------
            # SHOW TRANSCRIPT
            # -------------------------

            with st.expander("Show Transcript"):
                st.write(transcript)

            # -------------------------
            # SUMMARY TIMER
            # -------------------------

            summary_start = time.time()

            with st.spinner("Generating AI summary..."):

                summary = summarize_text(transcript)

            summary_end = time.time()

            summary_time = round(
                summary_end - summary_start,
                2
            )

            st.success(
                f"Summary generated in {summary_time} seconds"
            )

            # -------------------------
            # TOTAL TIME
            # -------------------------

            total_end = time.time()

            total_time = round(
                total_end - total_start,
                2
            )

            st.info(
                f"Total execution time: {total_time} seconds"
            )

            # -------------------------
            # SHOW SUMMARY
            # -------------------------

            st.subheader("AI Summary")

            st.write(summary)

        except Exception as e:

            st.error(f"Error: {str(e)}")