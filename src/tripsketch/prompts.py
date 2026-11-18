"""Step 4 (CO4): few-shot and chain-of-thought prompts."""

FEW_SHOT_PROMPT = """You are a travel guide card writer for first-time travellers.
Example 1
Summary: Alleppey in Kerala is famous for its backwaters, where people travel on houseboats.
Q: Why is Alleppey famous?
A: For its calm backwaters and houseboat stays.
Example 2
Summary: {summary}
Q:"""

COT_PROMPT = """Summary: {summary}
Let's think step by step. First list the two most useful facts for a traveller.
Then check that the answer below agrees with the summary.
Answer: {answer}
Finally give one short, practical travel tip that is easy to remember.
Travel tip:"""


def fnGenerateCard(strSummary, fnLLM):
    """Few-shot prompt gives Q&A; chain-of-thought prompt gives the tip."""
    strQA = "Q:" + fnLLM(FEW_SHOT_PROMPT.format(summary=strSummary))
    strTip = fnLLM(COT_PROMPT.format(summary=strSummary, answer=strQA))
    return strQA, strTip
