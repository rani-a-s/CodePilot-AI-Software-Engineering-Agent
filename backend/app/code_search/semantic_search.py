import numpy as np

from backend.app.code_indexer.indexer import index_codebase
from backend.app.embeddings.embedder import create_embedding


# Store generated embeddings in memory
embedding_cache = {}


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """Calculate cosine similarity between two vectors."""

    a = np.array(vector_a)
    b = np.array(vector_b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def get_code_embedding(code: str) -> list[float]:
    """Create an embedding and cache it for reuse."""

    if code not in embedding_cache:
        embedding_cache[code] = create_embedding(code)

    return embedding_cache[code]


def semantic_search(
    repository_path: str,
    query: str,
    limit: int = 5,
) -> dict:
    """Search code chunks using semantic similarity."""

    if not query.strip():
        return {
            "query": query,
            "total_matches": 0,
            "results": [],
        }

    query_embedding = create_embedding(query)

    index = index_codebase(repository_path)

    results = []

    for chunk in index["chunks"]:
        code_embedding = get_code_embedding(chunk["code"])

        similarity = cosine_similarity(
            query_embedding,
            code_embedding,
        )

        result = chunk.copy()
        result["similarity"] = round(similarity, 4)

        results.append(result)

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    return {
        "query": query,
        "total_matches": len(results),
        "results": results[:limit],
    }