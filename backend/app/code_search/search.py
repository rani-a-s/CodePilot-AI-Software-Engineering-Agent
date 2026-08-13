import re

from backend.app.code_indexer.indexer import index_codebase


def tokenize(text: str) -> set[str]:
    """Convert text into lowercase search words."""

    text = text.replace("_", " ")
    text = text.replace("-", " ")

    return set(
        re.findall(
            r"[a-zA-Z0-9]+",
            text.lower(),
        )
    )


def calculate_score(
    query_words: set[str],
    chunk: dict,
) -> int:
    """Calculate weighted relevance for a code chunk."""

    symbol = chunk.get("symbol", "").lower()
    file_path = chunk.get("file", "").lower()
    code = chunk.get("code", "").lower()

    symbol_words = tokenize(symbol)
    file_words = tokenize(file_path)
    code_words = tokenize(code)

    score = 0

    # Strongest: function/class name
    symbol_matches = query_words.intersection(symbol_words)
    score += len(symbol_matches) * 10

    # Medium: file path
    file_matches = query_words.intersection(file_words)
    score += len(file_matches) * 5

    # Weakest: source code
    code_matches = query_words.intersection(code_words)
    score += len(code_matches)

    # Bonus for an exact normalized symbol match
    normalized_query = " ".join(sorted(query_words))
    normalized_symbol = " ".join(sorted(symbol_words))

    if normalized_query == normalized_symbol:
        score += 20

    return score


def search_code(
    repository_path: str,
    query: str,
    limit: int = 5,
) -> dict:
    """Search indexed code chunks using weighted relevance."""

    if not query.strip():
        return {
            "query": query,
            "total_matches": 0,
            "results": [],
        }

    query_words = tokenize(query)

    index = index_codebase(repository_path)

    scored_results = []

    for chunk in index["chunks"]:

        score = calculate_score(
            query_words,
            chunk,
        )

        if score > 0:
            result = chunk.copy()
            result["score"] = score
            scored_results.append(result)

    scored_results.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return {
        "query": query,
        "total_matches": len(scored_results),
        "results": scored_results[:limit],
    }