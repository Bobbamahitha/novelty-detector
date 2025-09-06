"""data_prep.py
Utilities to load and prepare patent / disclosure text data for the novelty detector.
"""
import pandas as pd
import re

def load_corpus(csv_path: str) -> pd.DataFrame:
    """Load sample patent corpus CSV. Expects columns: id, title, abstract, claims, publication_date"""
    df = pd.read_csv(csv_path)
    # combine fields into a single text field
    df['text'] = (df['title'].fillna('') + '. ' + df['abstract'].fillna('') + ' ' + df['claims'].fillna('')).str.strip()
    return df[['id','title','abstract','claims','text','publication_date']]

def simple_clean(text: str) -> str:
    """Basic cleaning: lowercase, remove extra whitespace and non-alphanumeric (keep some punctuation)."""
    if not isinstance(text, str):
        return ''
    text = text.lower().strip()
    # remove weird characters but keep basic punctuation for tokenization if needed
    text = re.sub(r'[^a-z0-9\s\.,\-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text
