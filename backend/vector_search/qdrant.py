from data import PRODUCT_CATALOG, SEMANTIC_EMBEDDINGS, TEST_QUERIES, TEXT_DOCUMENTS
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    Range,
    VectorParams,
)


def main():
    # -------------------------
    # Connect to Qdrant
    # -------------------------
    client = QdrantClient(":memory:")  # In-memory instance for demo purposes

    # -------------------------
    # Initialize collections
    # -------------------------
    for collection_name, collection_data in zip(
        ["document", "product", "semantic"],
        [TEXT_DOCUMENTS, PRODUCT_CATALOG, SEMANTIC_EMBEDDINGS],
    ):
        # Check if collection exists and rebuild
        if client.collection_exists(collection_name=collection_name):
            client.delete_collection(collection_name=collection_name)
            print(f"Deleted existing collection: {collection_name}")

        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=10, distance=Distance.COSINE),
        )
        print(f"Created new collection: {collection_name}")  # Add data

        points = [
            PointStruct(
                id=i,
                vector=data["vector"],
                payload={k: v for k, v in data.items() if k not in ["vector"]},
            )
            for i, data in enumerate(collection_data)
        ]

        client.upsert(collection_name=collection_name, points=points)
        print(f"Added {len(points)} points to collection: {collection_name}")

    # -------------------------
    # Vector search
    # -------------------------
    for collection_name, query in zip(
        ["document", "product", "semantic"],
        [
            TEST_QUERIES["document_query"],
            TEST_QUERIES["product_query"],
            TEST_QUERIES["semantic_query"],
        ],
    ):
        search_results = client.query_points(
            collection_name=collection_name,
            query=query,
            limit=3,
            with_payload=True,
        )
        print(f"\n--- Vector search results for {collection_name} collection ---")
        for result in search_results.points:
            assert result.payload is not None, "Payload should not be None"
            print(
                f"ID: {result.id}, Score: {result.score:.4f}, Payload: {result.payload}"
            )

    # -------------------------
    # Filtered search for product collection - by category
    # -------------------------
    print("\n--- Filtered search for product collection - by category ---")
    search_results = client.query_points(
        collection_name="product",
        query_filter=Filter(
            must=[FieldCondition(key="category", match=MatchValue(value="Electronics"))]
        ),
        limit=3,
    )
    results = search_results.points

    for result in results:
        assert result.payload is not None, "Payload should not be None"
        print(
            f"ID: {result.id}, Score: {result.score:.4f}, Name: {result.payload['name']}, Category: {result.payload['category']}"
        )

    # -------------------------
    # Tag search for document collection
    # -------------------------
    print("\n--- Tag search for document collection ---")
    search_results = client.query_points(
        collection_name="document",
        query_filter=Filter(
            must=[FieldCondition(key="tags", match=MatchValue(value="AI"))]
        ),
        limit=3,
    )
    results = search_results.points

    for result in results:
        assert result.payload is not None, "Payload should not be None"
        print(
            f"ID: {result.id}, Score: {result.score:.4f}, Title: {result.payload['title']}, Tags: {result.payload['tags']}"
        )

    # -------------------------
    # Complex filtered search for product collection - price range and stock
    # -------------------------
    print(
        "\n--- Complex filtered search for product collection - price range and stock ---"
    )
    search_results = client.query_points(
        collection_name="product",
        query=TEST_QUERIES["product_query"],
        query_filter=Filter(
            must=[
                FieldCondition(key="price", range=Range(gte=1000.0, lte=3000.0)),
                FieldCondition(key="in_stock", match=MatchValue(value=True)),
            ]
        ),
        limit=3,
    )
    results = search_results.points

    for result in results:
        assert result.payload is not None, "Payload should not be None"
        print(
            f"ID: {result.id}, Score: {result.score:.4f}, Name: {result.payload['name']}, Price: {result.payload['price']}, In Stock: {result.payload['in_stock']}"
        )


if __name__ == "__main__":
    main()
