# src/chunking.py

from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_texts(texts: List[str], chunk_size: int = 300, chunk_overlap: int = 50) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " "],
        length_function=len
    )
    all_chunks = []
    for doc in texts:
        chunks = splitter.split_text(doc)
        all_chunks.extend(chunks)
    return all_chunks
