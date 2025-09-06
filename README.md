# Automated Novelty Detection System for Technical Inventions

A compact prototype that helps evaluate whether a new invention disclosure contains features not present in existing patent literature — useful as a screening tool during prior-art checks and to highlight candidate novel terms for patent drafting.

---

## Key features
- Ingests a small corpus of patent abstracts/claims and a new disclosure.
- Computes TF-IDF vectors and cosine similarity to find top matching prior art.
- Extracts **candidate novel terms** where the disclosure has high TF-IDF weight but the top matches do not.
- Produces a Markdown report (`novelty_report.md`) summarizing matches and novel-term candidates.

---

## Quick start (30–60 seconds)

> Tested on Windows / macOS / Linux. Example commands assume you are in the project root (the folder that contains `run_demo.py`).

1. **Create & activate a virtual environment**
   - macOS / Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  # one-time for current shell
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (Command Prompt):
     ```bat
     python -m venv venv
     venv\Scripts\activate.bat
     ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the demo**
   python run_demo.py
Output will print top matches and candidate novel terms and will create novelty_report.md.
**Example output (from a sample run)**

**Terminal output**
Top matches:
1 0.5874892077791422
3 0.16577017249717974
4 0.04897585294217635

Candidate novel terms:
cycle 0.227511 0.272686 0.045175
duty 0.227511 0.272686 0.045175
duty cycle 0.227511 0.272686 0.045175
dynamically 0.227511 0.272686 0.045175
energy 0.227511 0.272686 0.045175
packet 0.227511 0.272686 0.045175
algorithm 0.227134 0.272686 0.045552
aware 0.212818 0.272686 0.059868
method scheduling 0.182336 0.272686 0.09035
packets 0.182336 0.272686 0.09035
scheduling packets 0.182336 0.272686 0.09035
scheduling 0.13716 0.272686 0.135526
battery 0.13603 0.272686 0.136656
method 0.091606 0.182621 0.091015
Wrote report to: novelty_report.md
