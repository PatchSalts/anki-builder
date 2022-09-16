from fugashi import Tagger

tagger = Tagger()

def segment_japanese(text: str):
    return tagger(text)