import uuid

import chromadb
from data import PRODUCT_CATALOG, SEMANTIC_EMBEDDINGS, TEST_QUERIES, TEXT_DOCUMENTS


def main():
    # -------------------------
    # Connect to Chroma
    # -------------------------
    client = chromadb.Client()  # In-memory instance for demo purposes

    # -------------------------
    # Initialize collections
    # -------------------------
    for collection_name, collection_data in zip(
        ["document", "product", "semantic"],
        [TEXT_DOCUMENTS, PRODUCT_CATALOG, SEMANTIC_EMBEDDINGS],
    ):

        # Check if collection exists and recreate
        try:
            client.delete_collection(name=collection_name)
            print(f"Deleted existing collection: {collection_name}")
        except:
            # Collection might not exist
            pass

        # Create collection
        collection = client.create_collection(
            name=collection_name,
            metadata={
                "hnsw:space": "cosine"
            },  # Using cosine similarity as in Qdrant example
        )
        print(f"Created new collection: {collection_name}")

        # Process data for adding to collection
        ids = []
        documents = []
        metadatas = []
        embeddings = []

        for i, data in enumerate(collection_data):
            ids.append(data.get("id", str(i)))
            documents.append(
                data.get("content", data.get("description", data.get("text", "")))
            )
            metadatas.append(
                {
                    k: (
                        ",".join([vv if isinstance(vv, str) else str(vv) for vv in v])
                        if isinstance(v, list)
                        else v
                    )
                    for k, v in data.items()
                    if k not in ["vector"]
                }
            )
            embeddings.append(data["vector"])

        # Add data to collection
        collection.add(
            ids=ids, documents=documents, metadatas=metadatas, embeddings=embeddings
        )
        print(f"Added {len(ids)} points to collection: {collection_name}")

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
        collection = client.get_collection(name=collection_name)
        search_results = collection.query(
            query_embeddings=[query],
            n_results=3,
            include=["metadatas", "distances"],
        )
        metadatas = search_results["metadatas"]
        distances = search_results["distances"]
        assert metadatas is not None, "Metadata should not be None"
        assert distances is not None, "Distances should not be None"
        print(f"\n--- Vector search results for {collection_name} collection ---")
        for metadata, distance in zip(metadatas[0], distances[0]):
            print(
                f"ID: {metadata['id']}, Distance: {distance:.4f}, Metadata: {metadata}"
            )

    # -------------------------
    # Filtered search for product collection - by category
    # -------------------------
    print("\n--- Filtered search for product collection - by category ---")
    product_collection = client.get_collection(name="product")

    search_results = product_collection.get(
        where={"category": "Electronics"},
        limit=3,
        include=["metadatas"],
    )

    metadatas = search_results["metadatas"]
    assert metadatas is not None, "Metadata should not be None"
    for metadata in metadatas:
        print(
            f"ID: {metadata['id']}, Name: {metadata['name']}, Category: {metadata['category']}"
        )

    # -------------------------
    # Tag search for document collection
    # -------------------------
    print("\n--- Tag search for document collection (Not supported) ---")
    # document_collection = client.get_collection(name="document")

    # In Chroma, we search for documents where "tags" array contains "AI"
    # We need to use $contains operator for array fields
    # search_results = document_collection.get(
    #     where={"tags": {"$contains": "AI"}},
    #     limit=3,
    #     include=["metadatas"],
    # )

    # metadatas = search_results["metadatas"]
    # assert metadatas is not None, "Metadata should not be None"
    # for metadata in metadatas:
    #     print(
    #         f"ID: {metadata['id']}, Title: {metadata['title']}, Tags: {metadata['tags']}"
    #     )

    # -------------------------
    # Complex filtered search for product collection - price range and stock
    # -------------------------
    print(
        "\n--- Complex filtered search for product collection - price range and stock ---"
    )
    product_collection = client.get_collection(name="product")

    search_results = product_collection.query(
        query_embeddings=[TEST_QUERIES["product_query"]],
        where={
            "$and": [
                {"price": {"$gte": 1000.0}},
                {"price": {"$lte": 3000.0}},
                {"in_stock": True},
            ]
        },
        n_results=3,
        include=["metadatas", "distances"],
    )

    metadatas = search_results["metadatas"]
    assert metadatas is not None, "Metadata should not be None"
    for metadata in metadatas[0]:
        print(
            f"ID: {metadata['id']}, Distance: {distance:.4f}, Name: {metadata['name']}, "
            f"Price: {metadata['price']}, In Stock: {metadata['in_stock']}"
        )


if __name__ == "__main__":
    main()
