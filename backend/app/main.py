from fastapi import FastAPI

app = FastAPI(
    title="CodePilot API",
    description="AI-Powered Software Engineering Agent",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "CodePilot AI Software Engineering Agent is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }