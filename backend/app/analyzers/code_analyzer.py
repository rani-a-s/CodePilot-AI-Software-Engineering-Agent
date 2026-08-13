import ast
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


def analyze_python_file(file_path: Path, repository_root: Path) -> dict:
    """Analyze a Python file using the Abstract Syntax Tree."""

    relative_file = file_path.relative_to(repository_root)

    try:
        source_code = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source_code)

    except (SyntaxError, OSError) as error:
        return {
            "file": relative_file.as_posix(),
            "error": str(error),
            "classes": [],
            "functions": [],
            "imports": [],
        }

    classes = []
    functions = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):
            methods = []

            for child in node.body:
                if isinstance(
                    child,
                    (ast.FunctionDef, ast.AsyncFunctionDef)
                ):
                    methods.append(child.name)

            classes.append({
                "name": node.name,
                "methods": methods,
                "line": node.lineno,
            })

        elif isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            functions.append({
                "name": node.name,
                "line": node.lineno,
            })

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    return {
        "file": relative_file.as_posix(),
        "classes": classes,
        "functions": functions,
        "imports": sorted(set(imports)),
    }


def analyze_codebase(repository_path: str) -> dict:
    """Analyze all Python files in a repository."""

    root = Path(repository_path).resolve()

    python_files = []

    for path in root.rglob("*.py"):

        if any(
            part in IGNORED_DIRECTORIES
            for part in path.parts
        ):
            continue

        python_files.append(path)

    results = []

    for python_file in python_files:
        results.append(
            analyze_python_file(
                python_file,
                root
            )
        )

    return {
        "total_python_files": len(python_files),
        "files": results,
    }