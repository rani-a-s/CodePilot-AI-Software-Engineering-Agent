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


def analyze_repository(repository_path: str) -> dict:
    """Analyze the basic structure of a software repository."""

    root = Path(repository_path).resolve()

    if not root.exists():
        raise FileNotFoundError(
            f"Repository path does not exist: {repository_path}"
        )

    files = []
    directories = set()
    extensions = {}

    for path in root.rglob("*"):
        if any(part in IGNORED_DIRECTORIES for part in path.parts):
            continue

        if path.is_dir():
            directories.add(str(path.relative_to(root)))
            continue

        if path.is_file():
            relative_path = str(path.relative_to(root))
            files.append(relative_path)

            filename = path.name.lower()

            if filename == ".env":
                extension = ".env"
            elif filename.startswith(".env."):
                extension = ".env"
            else:
                extension = path.suffix.lower() or "[no extension]"

            extensions[extension] = extensions.get(extension, 0) + 1

    return {
        "repository": root.name,
        "total_files": len(files),
        "total_directories": len(directories),
        "file_extensions": extensions,
        "files": files,
    }