# src/vector_store.py

import faiss
import pickle
import os
import numpy as np

def create_faiss_index(embeddings: np.ndarray):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_faiss_index(index, path="vector_store/faiss_index/index.faiss"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    faiss.write_index(index, path)

def save_metadata(metadata, path="vector_store/faiss_index/metadata.pkl"):
    with open(path, "wb") as f:
        pickle.dump(metadata, f)

def load_faiss_index(path="vector_store/faiss_index/index.faiss"):
    return faiss.read_index(path)

def load_metadata(path="vector_store/faiss_index/metadata.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)
  
