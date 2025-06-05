# 🧠 RAG Technical Document Assistant

A lightweight Retrieval-Augmented Generation (RAG) app built using LangChain, OpenAI GPT-4, FAISS, and Streamlit.

Ask questions across any set of internal documents — and get accurate, AI-powered answers grounded in your data.

---

## 💡 Features

- 📄 Load `.txt` or `.md` technical files
- 🧠 Embed and store content with OpenAI + FAISS
- 🔍 Ask natural language questions
- 💬 GPT answers based on your actual content (no hallucinations)
- 🌐 Simple UI with Streamlit

---

## 🛠️ Tech Stack

- `LangChain` for chunking and chaining
- `OpenAI GPT-4` for intelligent responses
- `FAISS` for vector similarity search
- `Streamlit` for the front-end
- `Python` + `venv` + `unstructured` + `langchain-community`

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Jayasudhaa/rag-tech_doc_assistant.git
cd rag-tech_doc_assistant

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your OpenAI API Key
export OPENAI_API_KEY=sk-xxxx  # On Windows: set OPENAI_API_KEY=sk-xxxx

# 5. Run the app
streamlit run rag_tech_doc_assistant.py
