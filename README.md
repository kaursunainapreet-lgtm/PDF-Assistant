# 📚 PDF AI Assistant
A simple AI-powered application that lets users upload PDF documents and ask questions about them in natural language.
Instead of manually reading long PDFs, users can upload a document and interact with it like a chatbot. The application retrieves the most relevant content from the PDF and uses a local AI model to generate answers.

---

## 🚀 Why I Built This

I wanted to explore how Retrieval-Augmented Generation (RAG) works in real-world applications.

This project combines PDF processing, information retrieval, and local Large Language Models (LLMs) to create a practical document assistant that runs entirely on a user's machine without relying on paid APIs.

---

##  Features

-  Upload PDF documents
-  Ask questions in natural language
-  Retrieve relevant information from the document
-  Generate context-aware answers
-  Runs completely locally using Ollama
-  No paid APIs required
-  Simple and easy-to-use Streamlit interface

---

##  Tech Stack

- Python
- Streamlit
- Ollama
- Phi-3
- PDF Processing Libraries
- Custom RAG Pipeline

---

## 🏗️ How It Works

1. Upload a PDF document.
2. The PDF text is extracted.
3. The text is divided into smaller chunks.
4. Relevant chunks are retrieved based on the user's question.
5. The retrieved context is sent to the Phi-3 model through Ollama.
6. The model generates an answer based on the document content.



## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/pdf-ai-assistant.git
cd pdf-ai-assistant
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama and Phi-3

Download Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull phi3
```

Verify installation:

```bash
ollama list
```

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 💡 Example Questions

- Summarize this document
- What are the key points?
- Explain the main concepts
- What recommendations are provided?
- Give me a short overview

---

## 📖 What I Learned

While building this project, I gained hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- PDF text extraction
- Text chunking techniques
- Local LLM deployment using Ollama
- Streamlit application development
- Building end-to-end AI applications

---

## 🔮 Future Improvements

Some features I would like to add in the future:

- Chat history
- Multiple PDF support
- Source references in answers
- Faster retrieval methods
- Dark mode UI
- Cloud deployment

---

## 👩‍💻 Author

**Sunainapreet Kaur**

Passionate about AI, NLP, Python, and building practical applications that solve real-world problems.

---

## ⭐ If You Like This Project

If you found this project interesting, consider giving it a star.

It motivates me to keep building and sharing more AI projects.
