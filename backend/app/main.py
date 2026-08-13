from fastapi import FastAPI

from backend.app.analyzers.repository_analyzer import analyze_repository
from backend.app.analyzers.technology_detector import detect_technologies
from backend.app.analyzers.code_analyzer import analyze_codebase
from backend.app.code_indexer.indexer import index_codebase
from backend.app.code_search.search import search_code


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