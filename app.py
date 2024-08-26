import os
import openai
import PyPDF2
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize_text_gpt(text):
    """Summarize the extracted text using GPT-4."""
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Summarize the following text:\n\n{text}\n\nSummary:",
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

def main():
    st.title("PDF Summarization Tool")

    pdf_file = st.file_uploader("Upload a PDF", type="pdf")

    if pdf_file:
        with st.spinner("Extracting and summarizing..."):
            text = extract_text_from_pdf(pdf_file)
            summary = summarize_text_gpt(text)
            st.write("Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()