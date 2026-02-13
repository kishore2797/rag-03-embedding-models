#!/usr/bin/env python3
"""
RAG Tutorial 03 — Embedding Models
Minimal example: embed sentences with Sentence-Transformers and compare similarity.
Run: pip install -r requirements.txt && python example.py
"""
from sentence_transformers import SentenceTransformer
import numpy as np


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    sentences = [
        "RAG combines retrieval with generation.",
        "Retrieval-augmented generation uses external documents.",
        "The weather is nice today.",
    ]
    embeddings = model.encode(sentences)
    print("Embedding shape:", embeddings.shape)  # (3, 384)

    # Similarity (cosine)
    q = model.encode(["What is RAG?"])[0]
    scores = np.dot(embeddings, q) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(q))
    for i, s in enumerate(sentences):
        print(f"  {scores[i]:.3f}  {s[:50]}...")
    print("\n→ First two sentences are semantically closer to 'What is RAG?' than the third.")


if __name__ == "__main__":
    main()
