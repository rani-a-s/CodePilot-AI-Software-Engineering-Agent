from fastapi import FastAPI

from backend.app.analyzers.repository_analyzer import analyze_repository
from backend.app.analyzers.technology_detector import detect_technologies
from backend.app.analyzers.code_analyzer import analyze_codebase
from backend.app.code_indexer.indexer import index_codebase
from backend.app.code_search.search import search_code
from backend.app.code_search.semantic_search import semantic_search
from backend.app.agent.agent import ask_codepilot

app = FastAPI(
    title="CodePilot API",
    description="AI-Powered Software Engineering Agent",
    version="0.3.0",
)


@app.get("/")
def root():
    return {
        "message": "CodePilot AI Software Engineering Agent is running",
        "version": "0.3.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/analyze")
def analyze():
    return analyze_repository(".")


@app.get("/technologies")
def technologies():
    return detect_technologies(".")


@app.get("/code-structure")
def code_structure():
    return analyze_codebase(".")

@app.get("/code-index")
def code_index():
    return index_codebase(".")

@app.get("/search")
def search(query: str, limit: int = 5):
    return search_code(
        ".",
        query,
        limit,
    )

@app.get("/semantic-search")
def semantic_search_endpoint(query: str, limit: int = 5):
    return semantic_search(
        ".",
        query,
        limit,
    )

@app.get("/ask")
def ask(question: str, limit: int = 3):
    return ask_codepilot(
        ".",
        question,
        limit,
    )