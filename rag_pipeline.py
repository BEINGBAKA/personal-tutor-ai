# rag_pipeline.py
import os
from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils.preprocessor import clean_text, split_into_chunks
import fitz  # PyMuPDF
import gc

# Use a lighter embedding model (~45 MB)
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# Load text from PDF
def load_pdf_text(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Load and preprocess the document (supports PDF and TXT)
def load_and_split_text(file_path: str, chunk_size: int = 250) -> List[str]:
    if file_path.endswith(".pdf"):
        raw_text = load_pdf_text(file_path)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

    cleaned = clean_text(raw_text)
    chunks = split_into_chunks(cleaned, chunk_size)
    return chunks

# Convert text chunks into embeddings
def embed_chunks(chunks: List[str]) -> List[np.ndarray]:
    vectors = model.encode(chunks)
    gc.collect()  # Free up memory
    return vectors

# Retrieve top-N most relevant chunks for a given query
def retrieve_similar_chunks(query: str, chunks: List[str], vectors: List[np.ndarray], top_n: int = 2) -> List[str]:
    query_vec = model.encode([query])[0]
    sims = cosine_similarity([query_vec], vectors)[0]
    top_indices = np.argsort(sims)[-top_n:][::-1]
    return [chunks[i] for i in top_indices]
