import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tripsketch.preprocess import fnSplitTopics


def test_split_gives_title_and_body():
    strNotes = Path(__file__).parent.parent.joinpath("sample_data", "travel_notes.txt").read_text()
    lstOut = fnSplitTopics(strNotes)
    assert [t for t, _ in lstOut] == ["Munnar", "Goa Beaches", "Amber Fort, Jaipur"]


def test_short_blocks_are_ignored():
    assert fnSplitTopics("Title\nToo short.\n\nOnly one line") == []
