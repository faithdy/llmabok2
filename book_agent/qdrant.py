import json
with open("book_agent/best-seller-books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# pip install sentence-transformers hf_xet
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

from qdrant_client.models import PointStruct
points = [PointStruct(id=idx+1, vector=model.encode(book["description"]).tolist(),
                      payload=book) for idx, book in enumerate(books)]

from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

if not client.collection_exists("books"):
    from qdrant_client.models import Distance, VectorParams

    client.create_collection(
        collection_name="books",
        vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(),
                                     distance=Distance.COSINE),
    )

    client.upsert(
        collection_name="books",
        points=points
    )

print("Book collection is ready.")