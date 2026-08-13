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


def should_ignore(path: Path) -> bool:
    """Check whether a path belongs to an ignored directory."""

    return any(
        part in IGNORED_DIRECTORIES
        for part in path.parts
    )


def get_source_lines(
    source_lines: list[str],
    start_line: int,
    end_line: int,
) -> str:
    """Extract source code using 1-based line numbers."""

    return "".join(
        source_lines[start_line - 1:end_line]
    )


def index_python_file(
    file_path: Path,
    repository_root: Path,
) -> list[dict]:
    """Extract functions and classes from a Python file."""

    try:
        source_code = file_path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        tree = ast.parse(source_code)

    except (SyntaxError, OSError):
        return []

    source_lines = source_code.splitlines(keepends=True)

    relative_path = file_path.relative_to(
        repository_root
    ).as_posix()

    chunks = []

    for node in ast.iter_child_nodes(tree):

        if isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef),
        ):
            start_line = node.lineno

            end_line = getattr(
                node,
                "end_lineno",
                node.lineno,
            )

            chunks.append({
                "file": relative_path,
                "symbol": node.name,
                "type": "function",
                "start_line": start_line,
                "end_line": end_line,
                "code": get_source_lines(
                    source_lines,
                    start_line,
                    end_line,
                ),
            })

        elif isinstance(node, ast.ClassDef):
            start_line = node.lineno

            end_line = getattr(
                node,
                "end_lineno",
                node.lineno,
            )

            chunks.append({
                "file": relative_path,
                "symbol": node.name,
                "type": "class",
                "start_line": start_line,
                "end_line": end_line,
                "code": get_source_lines(
                    source_lines,
                    start_line,
                    end_line,
                ),
            })

    return chunks


def index_codebase(repository_path: str) -> dict:
    """Index Python source code in a repository."""

    root = Path(repository_path).resolve()

    all_chunks = []

    for file_path in root.rglob("*.py"):

        if should_ignore(file_path):
            continue

        file_chunks = index_python_file(
            file_path,
            root,
        )

        all_chunks.extend(file_chunks)

    return {
        "total_chunks": len(all_chunks),
        "chunks": all_chunks,
    }