from textblob import TextBlob

import wikipedia

def search_wikipedia(name):
    print(f"Searching for {name}")
    return wikipedia.search(name)

def summary_wikipedia(name):
    print(f"summarizing {name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """"Get text objects and returns"""
    
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """finds wikipedia and return back phrases"""
    
    text = summary_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases

# GSW_text = wikipedia.summary("Golden State Warriors")
# print(GSW_text)