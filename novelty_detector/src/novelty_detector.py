"""novelty_detector.py
Implements a TF-IDF based novelty detector that compares a disclosure against a patent corpus
and returns top matches and candidate novel terms.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class NoveltyDetector:
    def __init__(self, max_features=5000, ngram_range=(1,2)):
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english', ngram_range=ngram_range)
        self.corpus_texts = None
        self.tfidf_matrix = None
        self.ids = None
        self.tdm_feature_names = None

    def fit(self, corpus_texts, ids=None):
        """Fit vectorizer on corpus_texts (list-like of strings)."""
        self.corpus_texts = corpus_texts
        self.ids = ids if ids is not None else list(range(len(corpus_texts)))
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus_texts)
        try:
            self.tdm_feature_names = self.vectorizer.get_feature_names_out()
        except AttributeError:
            self.tdm_feature_names = self.vectorizer.get_feature_names()

    def query(self, disclosure_text, top_k=5, n_novel_terms=10):
        """Query with a disclosure string. Returns:
        - top_k matches as list of tuples (id, score, snippet)
        - list of novel term candidates (term, score_diff)
        """
        if self.tfidf_matrix is None:
            raise ValueError('Call fit() with a corpus before querying.')
        q_vec = self.vectorizer.transform([disclosure_text])
        sims = cosine_similarity(q_vec, self.tfidf_matrix).flatten()
        top_idx = np.argsort(sims)[::-1][:top_k]
        top_matches = [(self.ids[i], float(sims[i]), self.corpus_texts[i][:500]) for i in top_idx]

        # extract candidate novel terms by comparing term weights
        q_arr = q_vec.toarray().flatten()  # shape (n_features,)
        top_tfidf = self.tfidf_matrix[top_idx].toarray()  # shape (top_k, n_features)
        mean_top = top_tfidf.mean(axis=0) if top_tfidf.size else np.zeros_like(q_arr)

        # score = q_tfidf - mean_top (higher = more unique in query)
        score_diff = q_arr - mean_top
        # map to terms
        terms = list(self.tdm_feature_names)
        term_scores = [(terms[i], float(score_diff[i]), float(q_arr[i]), float(mean_top[i])) for i in range(len(terms)) if q_arr[i] > 0]
        # sort by score_diff descending
        term_scores = sorted(term_scores, key=lambda x: x[1], reverse=True)
        novel_terms = [(t, round(diff,6), round(qtf,6), round(mtop,6)) for t,diff,qtf,mtop in term_scores[:n_novel_terms] if diff>0]

        return {"top_matches": top_matches, "novel_terms": novel_terms}
