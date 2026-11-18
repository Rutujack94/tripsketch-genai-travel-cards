"""Step 3 (CO3): BART summarisation."""
from functools import lru_cache

from .config import SUMMARY_MODEL


@lru_cache(maxsize=1)
def fnGetSummariser():
    from transformers import pipeline
    return pipeline("summarization", model=SUMMARY_MODEL)


def fnSummarise(strTopic):
    """Shorten the text to two or three sentences with BART."""
    dictOut = fnGetSummariser()(strTopic, max_length=70, min_length=25, do_sample=False)
    return dictOut[0]["summary_text"]
