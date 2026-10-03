# RAG PDF Chat 🤖

A RAG-based chatbot that answers questions from any PDF file using **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Groq API**. Built with **Streamlit**.

## ✨ Features

- 📄 Upload any PDF file
- 💬 Ask questions in Persian
- 🚀 Fast responses with Groq API
- 🌍 Multilingual embeddings (HuggingFace)
- 🎯 Accurate answers based on PDF content
- 🎨 Clean and simple Streamlit UI
- 🔒 Secure API key with Streamlit Secrets

## 🏗️ Architecture

```

PDF → Chunking → Embeddings → FAISS → Retrieval → Groq LLM → Answer

```

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core language |
| Streamlit | Web UI |
| LangChain | RAG framework |
| Groq API (GPT-OSS 20B) | LLM for answers |
| HuggingFace Embeddings | Multilingual vectors |
| FAISS | Vector database |
| PyPDF | PDF reader |

## 📋 Requirements

- Python 3.10+
- Groq API Key (free at [console.groq.com](https://console.groq.com))

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/seyyed-33/RAG-PDF-Chat.git
cd RAG-PDF-Chat
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .streamlit/secrets.toml file:

```toml
GROQ_API_KEY = "your_api_key_here"
```

4. Run the app:

```bash
streamlit run app.py
```

💡 How it Works

1. User uploads a PDF file
2. PDF is split into small chunks (300 chars)
3. Each chunk is converted to a vector (embedding)
4. Vectors are stored in FAISS database
5. When a question is asked, relevant chunks are retrieved
6. Groq LLM generates an answer based on retrieved context

📚 What I Learned

· Building RAG systems with LangChain
· Working with vector databases (FAISS)
· Multilingual embeddings for Persian
· API integration with Groq
· Building Streamlit web apps
· Handling secrets securely
· Deploying AI applications

## 🔗 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rag-pdf-chat-lyy3app2azptagyvfoscoxy.streamlit.app)

📝 License

This project is open source and available for learning purposes.

👨‍💻 Author

Seyyed Saleh Roodbari Zadeh

· GitHub: @seyyed-33
· Email: salehroodbari@gmail.com
