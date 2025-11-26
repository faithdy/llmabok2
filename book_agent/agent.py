from google.adk.agents import Agent
from typing import Optional
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

from qdrant_client import QdrantClient
from qdrant_client.models import Filter, MatchValue, FieldCondition
client = QdrantClient()


def search_books(query: str, top_k: int = 1, query_filter: Optional[dict] = None):
    """
    Search for books in the Qdrant collection based on the query.

    Args:
        query (str): The search query.
        top_k (int): The number of top results to return.
        query_filter:
            - Exclude vectors which doesn't fit given conditions.
            - If `None` - search among all vectors

    Examples:
    `Search with filter`::
        search_books(
            query = "search for red books",
            top_k = 1,
            query_filter=Filter(
                must=[
                    {
                        key="color",
                        value="red"
                    }
                ]
            )
        )            

    Returns:
        list: A list of book payloads matching the query.
    """
    query_vector = model.encode(query).tolist()
    if query_filter is not None:
        print(query_filter)
        query_filter = Filter(
            must=[
                FieldCondition(key=key, match=MatchValue(value=value))
                for key, value in query_filter.get('must', {}).items()
            ],
            must_not=[
                FieldCondition(key=key, match=MatchValue(value=value))
                for key, value in query_filter.get('must_not', {}).items()
            ]
        )
    search_result = client.search(
        collection_name="books",
        query_vector=query_vector,
        limit=top_k,
        query_filter=query_filter
    )
    return [hit.payload for hit in search_result]

root_agent = Agent(
    name="book_agent",
    model="gemini-2.5-flash",
    instruction="사용자의 베스트셀러에 관한 질문에 대해 **search_books** 툴을 사용하여 답하세요.",
    tools=[search_books],
)

if __name__ == '__main__':
    books = search_books(query="추천해줘.", query_filter=Filter(must_not=[
        FieldCondition(key="category", match=MatchValue(value="소설"))
    ]))
    for book in books:
        print(book)

