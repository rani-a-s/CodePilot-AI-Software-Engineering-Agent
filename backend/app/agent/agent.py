from backend.app.code_search.semantic_search import semantic_search


def ask_codepilot(
    repository_path: str,
    question: str,
    limit: int = 3,
) -> dict:
    """Answer a developer question using relevant code context."""

    search_results = semantic_search(
        repository_path,
        question,
        limit,
    )

    results = search_results["results"]

    if not results:
        return {
            "question": question,
            "answer": "I could not find relevant code for this question.",
            "sources": [],
        }

    top_result = results[0]

    answer = (
        f"The most relevant code is the `{top_result['symbol']}` "
        f"{top_result['type']} in `{top_result['file']}` "
        f"(lines {top_result['start_line']}-{top_result['end_line']}). "
        f"It has a semantic similarity score of "
        f"{top_result['similarity']}."
    )

    return {
        "question": question,
        "answer": answer,
        "sources": results,
    }