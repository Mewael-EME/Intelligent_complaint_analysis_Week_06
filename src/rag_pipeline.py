# src/rag_pipeline.py

import numpy as np
from src.embedder import load_embedding_model, get_embeddings
from src.vector_store import load_faiss_index, load_metadata
from src.prompt_template import build_prompt
from transformers import pipeline


# Load everything needed once
embedding_model = load_embedding_model()
faiss_index = load_faiss_index()
metadata = load_metadata()

# Load LLM for response generation
llm = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", max_new_tokens=512)

def retrieve_top_k_chunks(query: str, k: int = 5):
    query_embedding = get_embeddings(embedding_model, [query])[0]
    query_embedding = np.array([query_embedding]).astype('float32')
    
    distances, indices = faiss_index.search(query_embedding, k)
    
    results = []
    for idx in indices[0]:
        results.append(metadata[idx]["chunk"])  # could include ID or product too
    return results

def generate_answer(question: str, k: int = 5):
    retrieved_chunks = retrieve_top_k_chunks(question, k)
    prompt = build_prompt(question, retrieved_chunks)

    # Use LLM to generate answer
    output = llm(prompt, do_sample=False)[0]["generated_text"]
    return output, retrieved_chunks

