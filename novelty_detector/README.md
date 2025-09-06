# Automated Novelty Detection System for Technical Inventions

This project is a compact, GitHub-ready prototype that demonstrates how to compare a **new invention disclosure** against a corpus of patent abstracts/research papers and extract **candidate novel terms** that may indicate inventive features.

## What this repo contains
- `data/sample_patents.csv` — small example corpus
- `src/data_prep.py` — load & basic text cleaning
- `src/novelty_detector.py` — TF-IDF based novelty detector
- `src/generate_report.py` — create a Markdown report of results
- `run_demo.py` — runnable demo that outputs results and writes `novelty_report.md`
- `requirements.txt` — Python dependencies

## Quick start (local)
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\\Scripts\\activate` on Windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
   *Note:* `sentence-transformers` is optional and required only if you plan to use BERT embeddings for semantic similarity.

3. Run demo:
   ```bash
   python run_demo.py
   ```
   You should see top matches printed and `novelty_report.md` generated.

## How it works (short)
1. Load & clean corpus text (title + abstract + claims).
2. Fit TF-IDF vectorizer on corpus.
3. For a new disclosure, compute TF-IDF vector and cosine similarity against corpus.
4. Identify candidate novel terms where the disclosure TF-IDF weight is high but average TF-IDF weight across the top-matching prior-art documents is low.

## Next steps & improvements
- Use embeddings (e.g., sentence-transformers) for semantic similarity rather than lexical TF-IDF.
- Add claim-level parsing and structural analysis (identify independent vs dependent claims).
- Incorporate patent metadata (IPC/CPC classes) to restrict prior-art search space.
- Add a web UI to enter disclosures and view highlighted novel terms.

## License
MIT
