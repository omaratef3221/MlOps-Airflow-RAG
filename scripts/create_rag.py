import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from scripts.process_csv import download_csv_from_s3

import warnings
warnings.filterwarnings('ignore')
def create_rag_file():
    # Load CSV
    csv_path = './data/raw_movies.csv'
    data = None
    try:
        data = pd.read_csv(csv_path)
    except:
        download_csv_from_s3()
        data = pd.read_csv(csv_path)
    
    # Load embedding model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    # Generate embeddings
    descriptions = data['description'].fillna("").tolist()
    embeddings = model.encode(descriptions, convert_to_numpy=True)
    
    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # Save FAISS index
    if not os.path.exists('./faiss_index'):
        os.makedirs('./faiss_index')
    faiss.write_index(index, './faiss_index/movies.index')
    
    print("FAISS index created and saved.")
    return "Success"

# create_rag_file()