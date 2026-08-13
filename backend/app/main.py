from fastapi import FastAPI

from backend.app.analyzers.repository_analyzer import analyze_repository
from backend.app.analyzers.technology_detector import detect_technologies
from backend.app.analyzers.code_analyzer import analyze_codebase


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