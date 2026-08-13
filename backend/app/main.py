from fastapi import FastAPI
from backend.app.analyzers.repository_analyzer import analyze_repository
from backend.app.analyzers.technology_detector import detect_technologies

app = FastAPI(
    title="CodePilot API",
    description="AI-Powered Software Engineering Agent",
    version="0.2.0",
)


@app.get("/")
def root():
    return {
        "message": "CodePilot AI Software Engineering Agent is running",
        "version": "0.2.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/technologies")
def technologies():
    return detect_technologies(".")