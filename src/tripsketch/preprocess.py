"""Step 1 (CO1): text cleaning and destination splitting."""
import re

from .config import MIN_BODY_CHARS


def fnEnsureNltk():
    """Download the NLTK data needed by this project (only the first time)."""
    import nltk
    for strName in ("punkt", "punkt_tab", "stopwords", "wordnet"):
        nltk.download(strName, quiet=True)


def fnPreprocess(strText):
    """Clean text: tokenise, remove stop words, lemmatise."""
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    fnEnsureNltk()
    objLemma = WordNetLemmatizer()
    setStop = set(stopwords.words("english"))
    lstTokens = nltk.word_tokenize(strText.lower())
    lstClean = [objLemma.lemmatize(tok) for tok in lstTokens
                if tok.isalpha() and tok not in setStop]
    return " ".join(lstClean)


def fnSplitTopics(strNotes):
    """Destinations are separated by blank lines; the first line is the title.

    Returns a list of (strTitle, strBody) tuples.
    """
    lstOut = []
    for strBlock in re.split(r"\n\s*\n", strNotes):
        lstParts = strBlock.strip().split("\n", 1)
        if len(lstParts) == 2 and len(lstParts[1].strip()) > MIN_BODY_CHARS:
            lstOut.append((lstParts[0].strip(), lstParts[1].strip()))
    return lstOut
