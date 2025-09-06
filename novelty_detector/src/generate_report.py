"""generate_report.py
Simple functions to create a Markdown report highlighting top matches and novel terms.
"""
from datetime import datetime

def generate_markdown_report(disclosure_title, disclosure_text, results, corpus_df=None, out_path='novelty_report.md'):
    md_lines = []
    md_lines.append(f"# Novelty Detection Report\n")
    md_lines.append(f"**Disclosure title:** {disclosure_title}\n")
    md_lines.append(f"**Date:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')}\n")
    md_lines.append("---\n")
    md_lines.append("## Disclosure (short)\n")
    md_lines.append(disclosure_text[:200] + '\n\n')
    md_lines.append("## Top Matches\n")
    for mid, score, snippet in results['top_matches']:
        md_lines.append(f"- **ID:** {mid} — **score:** {score:.4f}\n\n  Snippet: {snippet[:400]}\n\n")
    md_lines.append("## Candidate Novel Terms\n")
    md_lines.append("Term | ScoreDiff | QueryTF | MeanTopTF\n")
    md_lines.append("--- | --- | --- | ---\n")
    for term, diff, qtf, mtop in results['novel_terms']:
        md_lines.append(f"{term} | {diff} | {qtf} | {mtop}\n")

    with open(out_path, 'w') as f:
        f.write('\n'.join(md_lines))
    return out_path
