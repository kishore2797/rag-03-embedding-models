# 🧬 RAG Tutorial 03 — Embedding Models

<p align="center">
  <a href="https://github.com/kishore2797/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-3_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/kishore2797/mastering-rag) tutorial series**  
> Previous: [02 — Chunking Strategies](https://github.com/kishore2797/rag-02-chunking-strategies) | Next: [04 — Vector Stores](https://github.com/kishore2797/rag-04-vector-stores)

---

## 🌍 Real-World Scenario

> You're building a product search engine. Users type "lightweight laptop for programming under $800" and expect relevant results. The embedding model is the brain behind this — it decides that "lightweight laptop" is semantically close to "ultrabook" and "MacBook Air." **Pick the wrong model** and your search returns desktops. **Pick an expensive one** and you burn $500/month on API calls for a simple demo. This tutorial helps you choose wisely.

---

## 🏗️ What You'll Build

A benchmarking dashboard that compares **11+ embedding models** (OpenAI, Cohere, and open-source) on the same datasets. Measure retrieval accuracy, latency, cost, and embedding quality — all from one interactive UI.

```
Dataset (queries + ground truth) ──→ 11 Models in parallel
  ├── OpenAI text-embedding-3 (small, large, ada)
  ├── Cohere embed-v3 (english, multilingual, light)
  └── Open-source: MiniLM, E5-small/base/large, BGE-large
──→ Compare: Precision@K, MRR, NDCG, latency, cost, UMAP viz
```

## 🔑 Key Concepts

- **Embeddings**: dense vector representations that capture semantic meaning
- **Dimension trade-offs**: 384 vs. 768 vs. 1536 dimensions (speed vs. quality)
- **IR metrics**: Precision@K, Recall@K, MRR, NDCG, MAP, Hit Rate
- **Asymmetric embeddings**: query and document use different encoding strategies
- **Isotropy**: how uniformly embeddings are distributed in vector space

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · Sentence-Transformers · OpenAI · Cohere |
| Frontend | React 19 · Vite · Tailwind CSS · Recharts · UMAP visualization |

## 🚀 Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # Add API keys (optional — open-source models work without)
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — select models, run benchmarks, compare results.

## 📦 Example

A minimal runnable example is in the `example/` folder:

```bash
cd example
pip install -r requirements.txt
python example.py
```

It embeds sentences with Sentence-Transformers and compares similarity to a query.

## 📖 What You'll Learn

1. How embedding models convert text to vectors
2. Which model to choose for your use case and budget
3. How to benchmark retrieval quality with standard IR metrics
4. The cost vs. quality trade-off between paid and open-source models
5. How embedding quality directly impacts RAG answer quality

## 📋 Prerequisites

- Python 3.11+ and Node.js 18+
- Concepts from [Tutorial 02](https://github.com/kishore2797/rag-02-chunking-strategies) (chunking)
- Optional: OpenAI / Cohere API keys (open-source models work without)

## ✏️ Exercises

1. **Domain-specific test**: Create 10 query-document pairs from your domain (medical, legal, code). Which model performs best on *your* data?
2. **Dimension experiment**: Compare the same model family at different dimensions (e.g., OpenAI small vs. large). Plot quality vs. storage cost.
3. **Speed test**: Embed 1,000 chunks with each model. Create a latency chart. At what scale does the local model become faster than the API?
4. **Multilingual test**: Try non-English queries. Which models maintain quality across languages?
5. **Stale embedding detection**: Embed the same text with two different model versions. How much do the vectors differ? (This matters for model upgrades.)

## ⚠️ Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Using a different model for queries vs. documents | Mixing `text-embedding-ada-002` for docs and `text-embedding-3-small` for queries | Always use the same model (and version) for both |
| Ignoring dimension size | 1536-dim model for a 100-document prototype is overkill | Start with 384-dim (MiniLM) for prototypes, scale up when needed |
| Not normalizing vectors | Some models output non-unit vectors; cosine similarity assumes unit vectors | Normalize embeddings to unit length before storing |
| Re-embedding entire corpus for each experiment | Costly and slow | Cache embeddings per model — only re-embed when chunks change |

## 📚 Further Reading

- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — Live benchmark of 100+ embedding models
- [Massive Text Embedding Benchmark](https://arxiv.org/abs/2210.07316) (Muennighoff et al., 2022) — The paper behind MTEB
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings) — Official OpenAI embedding docs
- [Sentence-Transformers Documentation](https://www.sbert.net/) — The go-to library for open-source embeddings
- [Cohere Embed v3](https://cohere.com/blog/introducing-embed-v3) — Multi-stage embedding with compression

## ➡️ Next Steps

With embeddings in hand, head to **[Tutorial 04 — Vector Stores](https://github.com/kishore2797/rag-04-vector-stores)** to learn where and how to store and search these vectors efficiently.

---

<p align="center">
  <sub>Part of <a href="https://github.com/kishore2797/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>
