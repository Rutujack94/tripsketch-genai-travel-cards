"""ROUGE evaluation of generated summaries (CO3)."""


def fnRouge(strReference, strGenerated):
    """Compare one summary with a reference summary."""
    from rouge_score import rouge_scorer
    objScorer = rouge_scorer.RougeScorer(["rouge1", "rougeL"], use_stemmer=True)
    return objScorer.score(strReference, strGenerated)


def fnAverageRouge(lstReferences, lstGenerated):
    """Average ROUGE-1 and ROUGE-L F1 over many summaries (values for report section 6.4)."""
    fltR1, fltRL = 0.0, 0.0
    for strRef, strGen in zip(lstReferences, lstGenerated):
        dictScore = fnRouge(strRef, strGen)
        fltR1 += dictScore["rouge1"].fmeasure
        fltRL += dictScore["rougeL"].fmeasure
    intN = max(1, len(lstGenerated))
    return {"rouge1": fltR1 / intN, "rougeL": fltRL / intN, "cards": len(lstGenerated)}
