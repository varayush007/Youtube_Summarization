import streamlit as st
from langchain_helper import summarize_youtube_video

st.title("Youtube Video Summarizer 🔉🔊")
video_url = st.text_input("Enter YouTube Video URL:")


if st.button("Summarize"):
    if video_url:
        yt_summary = summarize_youtube_video(video_url)
        st.subheader("Answer")
        st.markdown(yt_summary)
    else:
        st.warning("Please enter a YouTube video URL.")
