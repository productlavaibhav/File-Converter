import streamlit as st
import re

def convert_srt_to_paragraph(uploaded_file):
    # Read content from the uploaded file
    srt_content = uploaded_file.getvalue().decode("utf-8")
    
    # Use regex to extract all dialogues, ignoring IDs and timestamps
    dialogues = re.findall(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\s*(.+?)(?=\n\n|\Z)', srt_content, re.DOTALL)
    paragraph = " ".join(dialogue.replace('\n', ' ') for dialogue in dialogues)
    
    return paragraph

def main():
    st.title("SRT to Text Converter")
    st.write("Upload your SRT file to convert it to plain text in paragraph format.")

    uploaded_file = st.file_uploader("Choose an SRT file", type="srt")
    if uploaded_file is not None:
        paragraph_text = convert_srt_to_paragraph(uploaded_file)
        st.write("### Converted Text")
        st.write(paragraph_text)

if __name__ == "__main__":
    main()
