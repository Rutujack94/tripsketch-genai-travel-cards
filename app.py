"""TripSketch - Streamlit interface (Step 6).

Run:  streamlit run app.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st

from tripsketch.illustrate import fnIllustrate
from tripsketch.keysentences import fnKeySentences
from tripsketch.llm import fnLLM
from tripsketch.preprocess import fnSplitTopics
from tripsketch.prompts import fnGenerateCard
from tripsketch.summarise import fnSummarise

st.set_page_config(page_title="TripSketch", page_icon="🧭")
st.title("TripSketch: Illustrated Travel Guide Cards")
st.caption("Content is AI-generated. Please verify it against your original notes.")

objFile = st.file_uploader("Upload travel notes (.txt)", type=["txt"])
if objFile:
    strNotes = objFile.getvalue().decode("utf-8")
    st.text_area("Preview of uploaded notes", strNotes[:300], height=120, disabled=True)
    if st.button("Generate cards"):
        lstTopics = fnSplitTopics(strNotes)
        if not lstTopics:
            st.warning("No destinations found. Separate destinations with a blank line "
                       "and put the destination name on the first line.")
        for strTitle, strBody in lstTopics:
            with st.spinner(f"Making card for {strTitle}..."):
                lstKey = fnKeySentences(strBody)
                strSummary = fnSummarise(" ".join(lstKey))
                strQA, strTip = fnGenerateCard(strSummary, fnLLM)
                objImg = fnIllustrate(strTitle)
            st.subheader(strTitle)
            st.image(objImg)
            st.write("**Summary:** " + strSummary)
            st.write(strQA)
            st.write("**Travel tip:** " + strTip)
