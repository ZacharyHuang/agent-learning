TEXT_DOCUMENTS = [
    {
        "id": "doc1",
        "content": "Machine learning is a field of study that gives computers the ability to learn without being explicitly programmed.",
        "title": "Introduction to Machine Learning",
        "author": "Samuel Jones",
        "category": "AI",
        "tags": ["machine learning", "AI", "computer science"],
        "date": "2023-05-10",
        "rating": 4.7,
        "vector": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    },
    {
        "id": "doc2",
        "content": "Deep learning is part of a broader family of machine learning methods based on artificial neural networks.",
        "title": "Deep Learning Fundamentals",
        "author": "Maria Chen",
        "category": "AI",
        "tags": ["deep learning", "neural networks", "AI"],
        "date": "2023-06-15",
        "rating": 4.8,
        "vector": [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1],
    },
    {
        "id": "doc3",
        "content": "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence.",
        "title": "Introduction to NLP",
        "author": "John Smith",
        "category": "AI",
        "tags": ["NLP", "language processing", "AI"],
        "date": "2023-04-22",
        "rating": 4.5,
        "vector": [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2],
    },
    {
        "id": "doc4",
        "content": "Quantum computing is the use of quantum phenomena such as superposition and entanglement to perform computation.",
        "title": "Quantum Computing Explained",
        "author": "Robert Miller",
        "category": "Quantum Physics",
        "tags": ["quantum", "computing", "physics"],
        "date": "2023-07-05",
        "rating": 4.9,
        "vector": [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2, 0.3],
    },
    {
        "id": "doc5",
        "content": "Blockchain is a growing list of records, called blocks, that are linked using cryptography.",
        "title": "Blockchain Fundamentals",
        "author": "Alice Johnson",
        "category": "Cryptocurrency",
        "tags": ["blockchain", "crypto", "technology"],
        "date": "2023-08-12",
        "rating": 4.6,
        "vector": [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1, 0.2, 0.3, 0.4],
    },
]

PRODUCT_CATALOG = [
    {
        "id": "prod1",
        "name": "iPhone 15 Pro Max",
        "category": "Electronics",
        "subcategory": "Smartphones",
        "description": "iPhone 15 Pro Max - Latest smartphone with cutting-edge features",
        "brand": "Apple",
        "price": 1299.99,
        "currency": "USD",
        "in_stock": True,
        "rating": 4.8,
        "features": ["A17 Bionic chip", "Pro camera system", "Face ID", "5G"],
        "colors": ["Silver", "Gold", "Graphite", "Blue"],
        "vector": [0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.5],
    },
    {
        "id": "prod2",
        "name": "Samsung Galaxy S24 Ultra",
        "category": "Electronics",
        "subcategory": "Smartphones",
        "description": "Galaxy S24 Ultra - Premium Android smartphone with S Pen",
        "brand": "Samsung",
        "price": 1199.99,
        "currency": "USD",
        "in_stock": True,
        "rating": 4.7,
        "features": ["Snapdragon processor", "S Pen", "120Hz display", "5G"],
        "colors": ["Black", "White", "Green", "Burgundy"],
        "vector": [0.85, 0.15, 0.75, 0.25, 0.65, 0.35, 0.55, 0.45, 0.45, 0.55],
    },
    {
        "id": "prod3",
        "name": "MacBook Pro 16-inch",
        "category": "Electronics",
        "subcategory": "Laptops",
        "description": "MacBook Pro 16 - Powerful laptop for creators and professionals",
        "brand": "Apple",
        "price": 2499.99,
        "currency": "USD",
        "in_stock": True,
        "rating": 4.9,
        "features": ["M3 chip", "Retina display", "32GB RAM", "1TB SSD"],
        "colors": ["Silver", "Space Gray"],
        "vector": [0.2, 0.8, 0.3, 0.7, 0.4, 0.6, 0.5, 0.5, 0.6, 0.4],
    },
    {
        "id": "prod4",
        "name": "Dell XPS 15",
        "category": "Electronics",
        "subcategory": "Laptops",
        "description": "Dell XPS 15 - Premium Windows laptop with InfinityEdge display",
        "brand": "Dell",
        "price": 1899.99,
        "currency": "USD",
        "in_stock": False,
        "rating": 4.6,
        "features": ["Intel Core i9", "NVIDIA RTX", "16GB RAM", "1TB SSD"],
        "colors": ["Platinum Silver", "Frost White"],
        "vector": [0.4, 0.6, 0.5, 0.5, 0.6, 0.4, 0.7, 0.3, 0.8, 0.2],
    },
    {
        "id": "prod5",
        "name": "Sony WH-1000XM5",
        "category": "Electronics",
        "subcategory": "Headphones",
        "description": "Sony WH-1000XM5 - Premium noise cancelling wireless headphones",
        "brand": "Sony",
        "price": 399.99,
        "currency": "USD",
        "in_stock": True,
        "rating": 4.8,
        "features": [
            "Noise cancellation",
            "40h battery",
            "Hi-Res Audio",
            "Touch controls",
        ],
        "colors": ["Black", "Silver"],
        "vector": [0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.5, 0.4, 0.6],
    },
]


SEMANTIC_EMBEDDINGS = [
    {
        "id": "query1",
        "text": "How do vector databases work?",
        "vector": [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95],
    },
    {
        "id": "query2",
        "text": "What is the best algorithm for similarity search?",
        "vector": [0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.2, 0.1],
    },
    {
        "id": "query3",
        "text": "Explain the differences between Chroma and Qdrant",
        "vector": [0.15, 0.25, 0.35, 0.45, 0.55, 0.45, 0.35, 0.25, 0.15, 0.05],
    },
    {
        "id": "query4",
        "text": "How to optimize vector search performance",
        "vector": [0.2, 0.3, 0.4, 0.5, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
    },
    {
        "id": "query5",
        "text": "Vector search vs traditional keyword search",
        "vector": [0.25, 0.35, 0.45, 0.55, 0.65, 0.55, 0.45, 0.35, 0.25, 0.15],
    },
]

"""
Sample query vectors for testing vector search functionalities.

- document_query: expected to return doc2.
- product_query: expected to return prod2.
- semantic_query: expected to return query2.

"""

TEST_QUERIES = {
    "document_query": [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.1],
    "product_query": [0.85, 0.2, 0.75, 0.3, 0.65, 0.4, 0.55, 0.5, 0.45, 0.6],
    "semantic_query": [0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.2, 0.1],
}
