# PDF Summarization Tool

This project is a PDF Summarization Tool built using Python, Streamlit, and OpenAI's GPT-4. The tool allows users to upload a PDF file, extracts text from it, and generates a concise summary using a large language model.

## Features

- **PDF Text Extraction**: Extracts text from uploaded PDF files using `PyPDF2`.
- **Text Summarization**: Summarizes the extracted text using OpenAI's GPT-4 model.
- **Streamlit Interface**: Provides an easy-to-use web interface for uploading PDFs and viewing summaries.

## Project Structure

```

pdf_summarizer/
│
├── .env
├── app.py
├── requirements.txt
└── README.md

```

- `.env`: Contains the OpenAI API key.
- `app.py`: Main Python file that runs the Streamlit app.
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `README.md`: This file, which contains information about the project.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pdf-summarizer.git
   cd pdf-summarizer
```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv pdf_summarizer_env
   source pdf_summarizer_env/bin/activate
   ```
3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Create a `.env` file** in the root directory of the project and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your-openai-api-key
   ```

## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```
2. **Access the application**:

   - After running the app, open your web browser and navigate to `http://localhost:8501/`.
   - Upload a PDF file, and the application will extract the text and display a summarized version.

## Example

Here's how the application works:

1. **Upload PDF**: The user uploads a PDF file via the Streamlit interface.
2. **Text Extraction**: The tool extracts the text from the PDF.
3. **Summarization**: The extracted text is summarized using OpenAI's GPT-4.
4. **Output**: The summary is displayed on the web interface.

## Dependencies

- **Python 3.7+**
- **Streamlit**: A framework for creating interactive web apps in Python.
- **PyPDF2**: A library for PDF text extraction.
- **OpenAI**: The API for accessing OpenAI's GPT-4 model.
- **python-dotenv**: A module to load environment variables from a `.env` file.

## Deployment

You can deploy this app on platforms like Heroku, AWS, or Streamlit Sharing. For deployment on Streamlit Sharing:

1. Push your code to a GitHub repository.
2. Connect your GitHub repository to Streamlit Sharing.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
