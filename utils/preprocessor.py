# utils/preprocessor.py
import re
from typing import List

def clean_text(text: str) -> str:
    # Remove extra whitespace, tabs, newlines
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def normalize_text(text: str) -> str:
    # Convert to lowercase and remove non-alphanumeric chars
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return text

def split_into_chunks(text: str, chunk_size: int = 300) -> List[str]:
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
