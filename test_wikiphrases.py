from nlplogic.core_nlp import search_wikipedia, summary_wikipedia, get_phrases

def test_get_phrases():
    assert "golden state" in get_phrases("Golden State Warriors")

def test_search_wikipedia():
    assert "Golden State Warriors" in search_wikipedia("Golden State Warriors")
