# src/embedder.py

from sentence_transformers import SentenceTransformer

def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    return model

def get_embeddings(model, texts):
    return model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
  
