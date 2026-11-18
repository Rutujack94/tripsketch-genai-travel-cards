"""Small wrapper that sends a prompt to the LLM API and returns the text reply.

Set OPENAI_API_KEY (and optionally OPENAI_MODEL) in your environment.
"""
import os
from functools import lru_cache


@lru_cache(maxsize=1)
def fnGetClient():
    from openai import OpenAI
    return OpenAI()  # reads OPENAI_API_KEY from the environment


def fnLLM(strPrompt):
    objResp = fnGetClient().chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": strPrompt}],
        temperature=0.4,
        max_tokens=150,
    )
    return objResp.choices[0].message.content.strip()
