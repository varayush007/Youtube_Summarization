# YouTube Video Summarizer with Streamlit and LangChain

This project provides a user-friendly web application for generating concise summaries of YouTube videos. 
It harnesses the power of LangChain and Google's Palm LLM to understand and condense video content.

## Key Features

- **Simple Interface:** Enter a YouTube video URL and click "Summarize" for a quick summary.
- **Efficient Summarization:** Leverages LangChain and advanced language models for effective text summarization.
- **Streamlit Integration:** Creates an easy-to-use web interface with Streamlit.

## How to Use

1. **Prerequisites:**
   - A Google Cloud Platform Account with a project and an API Key. See instructions here: https://cloud.google.com/docs/authentication/getting-started
   - Python 3.7+ and required libraries: `streamlit`, `langchain`, `youtube_transcript_api`, `dotenv`. Install these with `pip install -r requirements.txt`

2. **Environment Variables:**
   - Create a `.env` file in the project's root directory.
   - Add a variable named `GOOGLE_API_KEY` and set its value to your Google API Key.

3. **Run the Streamlit App:**
   - From your terminal, navigate to the project directory.
   - Execute `streamlit run main.py`

## Demo

![image](https://github.com/varayush007/Youtube_Summarization/assets/108609442/e661e127-c479-42f2-907a-2ed443a76445)


## Project Structure

- **main.py:** Contains the Streamlit application code for the user interface and logic.
- **langchain_helper.py:** Houses the functions for loading the YouTube transcript, text splitting, and summary generation via LangChain.
- **.env:** Stores your sensitive Google API key.
- **requirements.txt:** Lists project dependencies.

## Notes

- The Google Palm LLM is currently in a research preview, so access to the API might be limited. Be sure to follow Google's guidelines.

## Contributing

We welcome contributions to improve this project! Feel free to open issues or submit pull requests.
