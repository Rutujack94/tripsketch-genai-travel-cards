"""Step 2 (CO1): key sentence extraction with SBERT and cosine similarity."""
from functools import lru_cache

import numpy as np

from .config import SBERT_MODEL, TOP_K_SENTENCES
from .preprocess import fnEnsureNltk


@lru_cache(maxsize=1)
def fnGetEncoder():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(SBERT_MODEL)


def fnKeySentences(strTopic, intTopK=TOP_K_SENTENCES):
    """Pick sentences closest to the destination centroid (cosine similarity)."""
    import nltk
    from sklearn.metrics.pairwise import cosine_similarity
    fnEnsureNltk()
    lstSent = nltk.sent_tokenize(strTopic)
    arrVec = fnGetEncoder().encode(lstSent)
    arrCentroid = arrVec.mean(axis=0, keepdims=True)
    arrScore = cosine_similarity(arrVec, arrCentroid).ravel()
    lstIdx = np.argsort(arrScore)[::-1][:intTopK]
    return [lstSent[i] for i in sorted(lstIdx)]
