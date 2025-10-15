# QnA Chatbot (Without Conversation History)

A minimal Q&A chatbot built using open-source models (Ollama) and LangChain.  
This chatbot responds to a single user query at a time (i.e. **no conversation context**).

---

## 🧠 Features

- Ask a question and get a direct answer — no memory of past messages  
- Built with **LangChain Prompt/Chains** + **Ollama model**  
- Easy-to-deploy **Streamlit** web app  
- Simple and lightweight — ideal for QA use cases without context retention  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- Ollama installed & running locally (or configured)  
- Access to the model you want (e.g. `gemma:2b`)  

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Gauravkumardhakad/QnA-chatbot-without-conversation-history.git
   cd QnA-chatbot-without-conversation-history
   ```

  ```bash
  python -m venv venv
  source venv/bin/activate     # on macOS / Linux
  venv\Scripts\activate        # on Windows
  ```

  ```bash
  pip install -r requirements.txt
  ```
### Inside .env file
- LANGCHAIN_API_KEY=your_langchain_api_key
- LANGCHAIN_PROJECT=your_project_name


