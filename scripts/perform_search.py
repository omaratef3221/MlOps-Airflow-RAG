import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def perform_search(query, index_path='./faiss_index/movies.index', top_k=5):
    # Load FAISS index
    index = faiss.read_index(index_path)
    
    # Load embedding model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    # Generate query embedding
    query_vector = model.encode([query], convert_to_numpy=True)
    
    # Search in the index
    distances, indices = index.search(query_vector, top_k)
    return indices, distances
