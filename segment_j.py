from fugashi import Tagger

tagger = Tagger()

def segment_japanese(text: str) -> list[str]:
    return tagger(text)