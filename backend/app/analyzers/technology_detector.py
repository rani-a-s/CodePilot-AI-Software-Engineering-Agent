from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".idea",
    ".vscode",
}


LANGUAGE_EXTENSIONS = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".h": "C/C++",
    ".hpp": "C++",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".sql": "SQL",
    ".html": "HTML",
    ".css": "CSS",
}


FRAMEWORK_INDICATORS = {
    "FastAPI": ["fastapi"],
    "Django": ["django"],
    "Flask": ["flask"],
    "React": ["react", "react-dom"],
    "Next.js": ["next"],
    "Express": ["express"],
    "Spring Boot": ["spring-boot"],
}


def should_ignore(path: Path) -> bool:
    """Check whether a path belongs to an ignored directory."""

    return any(
        part in IGNORED_DIRECTORIES
        for part in path.parts
    )


def detect_languages(repository_path: str) -> dict:
    """Detect programming languages based on file extensions."""

    root = Path(repository_path).resolve()
    language_counts = {}

    for path in root.rglob("*"):

        if should_ignore(path):
            continue

        if not path.is_file():
            continue

        extension = path.suffix.lower()

        if extension in LANGUAGE_EXTENSIONS:
            language = LANGUAGE_EXTENSIONS[extension]

            language_counts[language] = (
                language_counts.get(language, 0) + 1
            )

    return language_counts


def find_dependency_files(repository_path: str) -> list:
    """Find dependency files anywhere inside the repository."""

    root = Path(repository_path).resolve()

    dependency_names = {
        "requirements.txt",
        "package.json",
        "pom.xml",
        "build.gradle",
        "build.gradle.kts",
    }

    dependency_files = []

    for path in root.rglob("*"):

        if should_ignore(path):
            continue

        if path.is_file() and path.name.lower() in dependency_names:
            dependency_files.append(path)

    return dependency_files


def detect_frameworks(repository_path: str) -> list:
    """Detect frameworks from dependency files."""

    detected_frameworks = set()

    dependency_files = find_dependency_files(repository_path)

    for dependency_file in dependency_files:

        try:
            content = dependency_file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

        except OSError:
            continue

        for framework, indicators in FRAMEWORK_INDICATORS.items():

            for indicator in indicators:

                if indicator in content:
                    detected_frameworks.add(framework)
                    break

    return sorted(detected_frameworks)


def detect_dependencies(repository_path: str) -> list:
    """Detect dependencies from common dependency files."""

    dependencies = set()

    dependency_files = find_dependency_files(repository_path)

    for dependency_file in dependency_files:

        filename = dependency_file.name.lower()

        # Python requirements.txt
        if filename == "requirements.txt":

            try:
                lines = dependency_file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines()

                for line in lines:

                    line = line.strip()

                    if not line:
                        continue

                    if line.startswith("#"):
                        continue

                    dependency = (
                        line.split("==")[0]
                        .split(">=")[0]
                        .split("<=")[0]
                        .split("~=")[0]
                        .strip()
                    )

                    if dependency:
                        dependencies.add(dependency)

            except OSError:
                continue

    return sorted(dependencies)


def detect_technologies(repository_path: str) -> dict:
    """Run all technology detection operations."""

    return {
        "languages": detect_languages(repository_path),
        "frameworks": detect_frameworks(repository_path),
        "dependencies": detect_dependencies(repository_path),
    }