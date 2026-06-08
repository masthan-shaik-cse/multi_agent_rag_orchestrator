import numpy as np

class OptimizedVectorStore:
    """
    Highly scalable RAG system utilizing vector databases to ground LLM responses 
    in proprietary technical documents.
    """
    def __init__(self, embedding_dim: int = 768):
        self.embedding_dim = embedding_dim
        # Using a simple in-memory numpy array to simulate Chroma/FAISS functionality
        self.document_embeddings = []
        self.document_metadata = []
        
    def add_documents(self, documents: list[str], embeddings: np.ndarray):
        """
        Indexes proprietary technical documents.
        """
        assert embeddings.shape[1] == self.embedding_dim, "Embedding dimension mismatch."
        for i, doc in enumerate(documents):
            self.document_embeddings.append(embeddings[i])
            self.document_metadata.append({"text": doc, "id": len(self.document_metadata)})
            
        print(f"Successfully indexed {len(documents)} documents into the vector store.")

    def search(self, query_embedding: np.ndarray, top_k: int = 3) -> list[dict]:
        """
        Performs optimized cosine similarity search to retrieve relevant context.
        """
        if not self.document_embeddings:
            return []
            
        doc_matrix = np.vstack(self.document_embeddings)
        
        # Compute Cosine Similarity
        dot_products = np.dot(doc_matrix, query_embedding)
        norms = np.linalg.norm(doc_matrix, axis=1) * np.linalg.norm(query_embedding)
        similarities = dot_products / (norms + 1e-9)
        
        # Get top-k indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                "score": similarities[idx],
                "content": self.document_metadata[idx]["text"]
            })
            
        return results

if __name__ == "__main__":
    store = OptimizedVectorStore()
    
    # Simulate adding docs
    dummy_docs = ["Technical specs for API v2", "Authentication flow architecture"]
    dummy_embeddings = np.random.randn(2, 768)
    store.add_documents(dummy_docs, dummy_embeddings)
    
    # Simulate retrieval
    query_emb = np.random.randn(768)
    res = store.search(query_emb, top_k=1)
    print("Retrieved Context:", res)
