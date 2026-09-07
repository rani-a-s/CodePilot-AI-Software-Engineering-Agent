# 🚀 CodePilot – AI-Powered Software Engineering Agent

CodePilot is an AI-powered software engineering assistant that analyzes a software repository, understands its code structure, detects technologies, indexes source code, and uses semantic search to answer developer questions.

## ✨ Features

- 📂 Repository structure analysis
- 🛠️ Technology and framework detection
- 🌳 Python AST-based code analysis
- 📑 Source code indexing
- 🔎 Keyword-based code search
- 🧠 AI-powered semantic code search
- 🤖 Developer question answering
- 📌 Relevant code source retrieval
- ⚡ FastAPI REST API
- 📚 Interactive Swagger API documentation
- 💻 Local AI embeddings using Sentence Transformers

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     Developer       │
                    │      Question       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   CodePilot Agent   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Semantic Search    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   AI Embeddings     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Code Indexer     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    AST Analyzer     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Repository Analyzer │
                    └─────────────────────┘
```

## 🛠️ Technology Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **Sentence Transformers**
- **NumPy**
- **Python AST**
- **Git**
- **GitHub**

## 📁 Project Structure

```text
CodePilot-AI-Software-Engineering-Agent/
│
├── backend/
│   ├── app/
│   │   │
│   │   ├── agent/
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   │
│   │   ├── analyzers/
│   │   │   ├── __init__.py
│   │   │   ├── repository_analyzer.py
│   │   │   ├── technology_detector.py
│   │   │   └── code_analyzer.py
│   │   │
│   │   ├── code_indexer/
│   │   │   ├── __init__.py
│   │   │   └── indexer.py
│   │   │
│   │   ├── code_search/
│   │   │   ├── __init__.py
│   │   │   ├── search.py
│   │   │   └── semantic_search.py
│   │   │
│   │   ├── embeddings/
│   │   │   ├── __init__.py
│   │   │   └── embedder.py
│   │   │
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── ai/
├── docs/
├── frontend/
├── tests/
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/rani-a-s/CodePilot-AI-Software-Engineering-Agent.git
cd CodePilot-AI-Software-Engineering-Agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r backend/requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server:

```powershell
uvicorn backend.app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Open the interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔌 API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Check CodePilot application information |
| `GET /health` | Check API health |
| `GET /analyze` | Analyze repository structure |
| `GET /technologies` | Detect programming languages and frameworks |
| `GET /code-structure` | Analyze Python code structure |
| `GET /code-index` | Generate indexed code chunks |
| `GET /search` | Perform keyword-based code search |
| `GET /semantic-search` | Perform AI-powered semantic code search |
| `GET /ask` | Ask CodePilot a developer question |

## 🧠 Semantic Search

CodePilot uses a local Sentence Transformer model to convert text and source code into numerical embeddings.

```text
Developer Question
        │
        ▼
Sentence Transformer
        │
        ▼
384-Dimensional Embedding
        │
        ▼
Cosine Similarity
        │
        ▼
Relevant Code
```

The current embedding model is:

```text
all-MiniLM-L6-v2
```

Semantic search allows CodePilot to find code based on **meaning**, rather than requiring an exact keyword match.

## 🤖 CodePilot Agent

The `/ask` endpoint allows developers to ask questions about the repository.

### Example Question

```text
Where is the API health check implemented?
```

### Example Response

```text
The most relevant code is the `health_check`
function in `backend/app/main.py`
(lines 27-30).
```

CodePilot also provides:

- Relevant source file
- Function or class name
- Start and end lines
- Source code
- Semantic similarity score

## 🔍 Example Workflow

```text
Developer Question
        ↓
     /ask
        ↓
CodePilot Agent
        ↓
Semantic Search
        ↓
Embedding Generation
        ↓
Cosine Similarity
        ↓
Relevant Code Chunks
        ↓
Developer-Friendly Answer
```

## 🎯 Project Goals

CodePilot is designed to evolve into a complete AI software engineering agent capable of:

- 🔎 Intelligent code search
- 🧠 Code understanding
- 🐛 Bug detection
- 💡 Code explanation
- 🧪 Test generation
- 🔐 Security analysis
- ✨ Code improvement suggestions
- 🤖 AI-assisted software development

## 📈 Current Development Status

```text
Repository Analyzer       ✅
Technology Detector       ✅
AST Code Analyzer         ✅
Code Indexer              ✅
Keyword Search            ✅
AI Embeddings             ✅
Semantic Search           ✅
CodePilot Agent           ✅
Vector Database           🔄
LLM Integration           🔄
Automated Testing         🔄
Frontend Dashboard        🔄
```

## 🚀 Future Enhancements

- Persistent vector database
- LLM-powered code explanations
- Automated bug detection
- AI-generated unit tests
- Security vulnerability detection
- Code refactoring suggestions
- GitHub repository integration
- Web-based developer dashboard
- Multi-language code analysis
- Agent-based software development workflows

## 👩‍💻 Author

**Rani Sankanur**

GitHub:  
https://github.com/rani-a-s

---

⭐ If you find this project interesting, consider giving it a star!