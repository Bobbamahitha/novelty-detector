"""run_demo.py
Minimal demo showing how to prepare corpus, fit detector, and query with a sample disclosure.
Usage: python run_demo.py
"""
import pandas as pd
from src.data_prep import load_corpus, simple_clean
from src.novelty_detector import NoveltyDetector
from src.generate_report import generate_markdown_report

def main():
    corpus = load_corpus('data/sample_patents.csv')
    corpus['clean_text'] = corpus['text'].apply(simple_clean)
    nd = NoveltyDetector(max_features=2000)
    nd.fit(corpus['clean_text'].tolist(), ids=corpus['id'].tolist())

    # sample new disclosure — replace with your actual disclosure when using.
    disclosure_title = 'Energy-aware Packet Scheduler for IoT'
    disclosure_text = ("A method for scheduling packets in an IoT network that dynamically adjusts duty cycle and uses an energy-aware "
                      "packet prioritization algorithm to extend battery lifetime for constrained devices.")
    clean_q = simple_clean(disclosure_text)
    results = nd.query(clean_q, top_k=3, n_novel_terms=15)

    print('Top matches:')
    for mid, score, snippet in results['top_matches']:
        print(mid, score)
    print('\nCandidate novel terms:')
    for term, diff, qtf, mtop in results['novel_terms']:
        print(term, diff, qtf, mtop)

    # write a markdown report
    out = generate_markdown_report(disclosure_title, disclosure_text, results, corpus_df=corpus, out_path='novelty_report.md')
    print(f'Wrote report to: {out}')

if __name__ == '__main__':
    main()
