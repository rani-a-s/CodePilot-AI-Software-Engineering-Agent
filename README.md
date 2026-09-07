# 🚀 CodePilot – AI-Powered Software Engineering Agent

CodePilot is an AI-powered software engineering assistant that analyzes software repositories, understands code structure, detects technologies, indexes source code, and uses semantic search to help developers find relevant code and answer repository-related questions.

---

## ✨ Features

- 📂 Repository structure analysis
- 🛠️ Programming language and framework detection
- 🌳 Python AST-based code analysis
- 📑 Source code indexing
- 🔎 Keyword-based code search
- 🧠 Semantic code search using AI embeddings
- 🤖 Developer question answering
- 📌 Relevant source code retrieval
- 📊 Similarity scoring for search results
- ⚡ FastAPI REST API
- 📚 Interactive Swagger API documentation
- 💻 Local embeddings using Sentence Transformers
- 🧪 Automated API testing using Pytest

---

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

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| FastAPI | REST API development |
| Uvicorn | Application server |
| Sentence Transformers | Text and code embeddings |
| NumPy | Vector and similarity calculations |
| Python AST | Python source-code analysis |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source-code hosting |

---

## 📁 Project Structure

```text
CodePilot-AI-Software-Engineering-Agent/
│
├── backend/
│   ├── app/
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
│   ├── __init__.py
│   └── test_codepilot.py
│
├── .env.example
├── .gitignore
└── README.md
```

---

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

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r backend/requirements.txt
```

---

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

---

## 🔌 API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Display CodePilot application information |
| `GET /health` | Check API health |
| `GET /analyze` | Analyze repository structure |
| `GET /technologies` | Detect programming languages and frameworks |
| `GET /code-structure` | Analyze Python code structure |
| `GET /code-index` | Generate indexed code chunks |
| `GET /search` | Perform keyword-based code search |
| `GET /semantic-search` | Perform semantic code search |
| `GET /ask` | Ask CodePilot a developer question |

---

## 🚀 Demo

CodePilot can be demonstrated through the interactive Swagger API.

### 1. Repository Analysis

Use:

```text
GET /analyze
```

CodePilot analyzes the repository and provides information about files, directories, and file types.

---

### 2. Technology Detection

Use:

```text
GET /technologies
```

This detects programming languages, frameworks, and technologies used by the repository.

---

### 3. Code Structure Analysis

Use:

```text
GET /code-structure
```

The AST analyzer identifies Python functions, classes, imports, and other structural information.

---

### 4. Semantic Code Search

Use:

```text
GET /semantic-search
```

Example query:

```text
find the function that checks if the API is healthy
```

CodePilot converts the query and indexed code into numerical embeddings and compares them using cosine similarity.

The most relevant code is returned based on semantic similarity.

---

### 5. Developer Q&A

Use:

```text
GET /ask
```

Example question:

```text
Where is the API health check implemented?
```

Example response:

```text
The most relevant code is the `health_check`
function in `backend/app/main.py`
(lines 27-30).
```

The response also provides:

- Relevant source file
- Function or class name
- Start and end lines
- Source code
- Semantic similarity score

---

## 🧠 How Semantic Search Works

CodePilot uses the local `all-MiniLM-L6-v2` Sentence Transformer model to convert developer queries and source-code chunks into numerical embeddings.

```text
Developer Query
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
Ranked Code Results
       │
       ▼
Most Relevant Code
```

This allows CodePilot to search code based on **meaning**, rather than depending only on exact keyword matches.

### Embedding Model

```text
all-MiniLM-L6-v2
```

The generated embeddings contain **384 dimensions**.

---

## 🤖 CodePilot Agent

The `/ask` endpoint provides a developer-friendly interface for repository questions.

### Example

**Question:**

```text
Where is the API health check implemented?
```

**CodePilot identifies:**

```text
Function: health_check
File: backend/app/main.py
```

It also returns the relevant source code and semantic similarity score.

> **Note:** The current agent is retrieval-based. It uses semantic search to retrieve relevant code and generates a structured developer-facing response. Full generative LLM integration is planned as a future enhancement.

---

## 🔍 Example Workflow

```text
Developer Question
        │
        ▼
      /ask
        │
        ▼
CodePilot Agent
        │
        ▼
Semantic Search
        │
        ▼
Embedding Generation
        │
        ▼
Cosine Similarity
        │
        ▼
Relevant Code Chunks
        │
        ▼
Developer-Friendly Answer
```

---

## 🧪 Automated Testing

CodePilot includes automated API tests using Pytest.

Run the tests with:

```powershell
pytest
```

Current test coverage includes:

- Root API endpoint
- Health check endpoint
- Semantic search
- CodePilot developer Q&A

Expected result:

```text
4 passed
```

---

## 📊 Current Development Status

```text
Repository Analyzer       ✅
Technology Detector       ✅
AST Code Analyzer         ✅
Code Indexer              ✅
Keyword Search            ✅
AI Embeddings             ✅
Semantic Search           ✅
CodePilot Agent           ✅
Automated Testing         ✅

Vector Database           🔄
LLM Integration           🔄
Frontend Dashboard        🔄
```

---

## 🎯 Project Goals

CodePilot is designed to evolve into a complete AI-assisted software engineering platform capable of:

- 🔎 Intelligent code search
- 🧠 Advanced code understanding
- 🐛 Automated bug detection
- 💡 Code explanation
- 🧪 Test generation
- 🔐 Security analysis
- ✨ Code improvement suggestions
- 🤖 AI-assisted software development
- 🔗 GitHub repository integration

---

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

---

## 👩‍💻 Author

**Rani Sankanur**

GitHub: `rani-a-s`

---

⭐ If you find this project interesting, consider giving it a star!
